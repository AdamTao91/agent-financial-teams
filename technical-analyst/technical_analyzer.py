#!/usr/bin/env python3
"""
Technical Analyst Agent - 技术分析核心模块
基于TA-Lib和pandas实现技术分析功能
"""

import akshare as ak
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class TechnicalAnalyzer:
    """技术分析核心类"""
    
    def __init__(self):
        self.symbol = None
        self.df = None
        
    def get_stock_data(self, symbol: str, period: str = "3mo") -> pd.DataFrame:
        """
        获取股票数据
        
        Args:
            symbol: 股票代码，如 "600519" 或 "600519.SH"
            period: 数据周期，默认3个月
            
        Returns:
            DataFrame with OHLCV data
        """
        self.symbol = symbol
        
        # 格式化代码
        if "." not in symbol:
            symbol = f"{symbol}.SH"  # 默认上交所
            
        try:
            # 使用akshare获取数据
            df = ak.stock_zh_a_hist(symbol=symbol.replace(".SH", ""), 
                                   start_date=(datetime.now() - timedelta(days=120)).strftime("%Y%m%d"),
                                   end_date=datetime.now().strftime("%Y%m%d"),
                                   adjust="qfq")
            df = df.sort_values('日期')
            df.set_index('日期', inplace=True)
            self.df = df
            return df
        except Exception as e:
            print(f"获取数据失败: {e}")
            return pd.DataFrame()
    
    # ==================== 均线系统 ====================
    
    def calculate_ma(self, periods: List[int] = [5, 10, 20, 30, 60, 120, 250]) -> Dict:
        """计算移动平均线"""
        if self.df is None:
            return {}
            
        ma_dict = {}
        for period in periods:
            ma_key = f"MA{period}"
            self.df[ma_key] = self.df['收盘'].rolling(window=period).mean()
            ma_dict[period] = round(self.df[ma_key].iloc[-1], 2) if len(self.df) >= period else None
            
        return ma_dict
    
    def ma_signals(self) -> Dict:
        """均线买卖信号"""
        if self.df is None or len(self.df) < 60:
            return {}
            
        ma5 = self.df['MA5'].iloc[-1]
        ma10 = self.df['MA10'].iloc[-1]
        ma20 = self.df['MA20'].iloc[-1]
        ma60 = self.df['MA60'].iloc[-1]
        close = self.df['收盘'].iloc[-1]
        
        signals = {
            "golden_cross": ma5 > ma10 and self.df['MA5'].iloc[-2] <= self.df['MA10'].iloc[-2],
            "death_cross": ma5 < ma10 and self.df['MA5'].iloc[-2] >= self.df['MA10'].iloc[-2],
            "bullish_arrangement": ma5 > ma10 > ma20 > ma60,
            "bearish_arrangement": ma5 < ma10 < ma20 < ma60,
            "price_above_ma20": close > ma20,
            "price_above_ma60": close > ma60,
        }
        
        # 葛兰威尔买卖法则
        signals["granville_signals"] = self._granville_signals()
        
        return signals
    
    def _granville_signals(self) -> List[Dict]:
        """葛兰威尔八大买卖法则"""
        signals = []
        
        if len(self.df) < 60:
            return signals
            
        ma20 = self.df['MA20'].values
        close = self.df['收盘'].values
        
        # 法则1: 均线向上，股价跌破均线是买进信号
        if ma20[-1] > ma20[-20] and close[-1] < ma20[-1] and close[-2] >= ma20[-2]:
            signals.append({"rule": 1, "signal": "bullish", "text": "均线向上，股价跌破MA20，买入"})
            
        # 法则2: 均线向下，股价突破均线是卖出信号
        if ma20[-1] < ma20[-20] and close[-1] > ma20[-1] and close[-2] <= ma20[-2]:
            signals.append({"rule": 2, "signal": "bearish", "text": "均线向下，股价突破MA20，卖出"})
            
        # 法则3: 股价连续上涨后，跌破均线后再次上涨是买进信号
        if close[-1] > ma20[-1] and close[-2] < ma20[-2]:
            signals.append({"rule": 3, "signal": "bullish", "text": "股价跌破MA20后再次上涨，买入"})
            
        # 法则4: 股价连续下跌后，突破均线后再次下跌是卖出信号
        if close[-1] < ma20[-1] and close[-2] > ma20[-2]:
            signals.append({"rule": 4, "signal": "bearish", "text": "股价突破MA20后再次下跌，卖出"})
            
        return signals
    
    # ==================== K线形态 ====================
    
    def candlestick_patterns(self) -> List[Dict]:
        """K线形态识别"""
        if self.df is None or len(self.df) < 5:
            return []
            
        patterns = []
        
        for i in range(-3, 0):
            o, h, l, c = self.df.iloc[i][['开盘', '最高', '最低', '收盘']]
            
            # 锤子线/上吊线
            body = abs(c - o)
            lower_shadow = min(o, c) - l
            upper_shadow = h - max(o, c)
            
            if lower_shadow > body * 2 and upper_shadow < body:
                if c > o:  # 锤子线（看涨）
                    patterns.append({"pattern": "锤子线", "index": i, "signal": "bullish"})
                else:  # 上吊线（看跌）
                    patterns.append({"pattern": "上吊线", "index": i, "signal": "bearish"})
                    
            # 吞没形态
            if i >= -2:
                prev_o, prev_c = self.df.iloc[i-1][['开盘', '收盘']]
                if (c > o and prev_c < prev_o and c > prev_o and o < prev_c) or \
                   (c < o and prev_c > prev_o and c < prev_o and o > prev_c):
                    signal = "bullish" if c > o else "bearish"
                    patterns.append({"pattern": "吞没形态", "index": i, "signal": signal})
                    
            # 射击之星/倒锤线
            if upper_shadow > body * 2 and lower_shadow < body:
                if c < o:  # 射击之星（看跌）
                    patterns.append({"pattern": "射击之星", "index": i, "signal": "bearish"})
                else:  # 倒锤线（看涨）
                    patterns.append({"pattern": "倒锤线", "index": i, "signal": "bullish"})
                    
        return patterns
    
    # ==================== 技术指标 ====================
    
    def calculate_macd(self, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict:
        """计算MACD"""
        if self.df is None or len(self.df) < slow:
            return {}
            
        ema_fast = self.df['收盘'].ewm(span=fast, adjust=False).mean()
        ema_slow = self.df['收盘'].ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).values
        histogram = macd.values - signal_line
        
        current_macd = macd.iloc[-1]
        current_signal = signal_line[-1]
        current_hist = histogram[-1]
        
        # 判断金叉死叉
        prev_macd = macd.iloc[-2]
        prev_signal = signal_line[-2]
        
        golden_cross = current_macd > current_signal and prev_macd <= prev_signal
        death_cross = current_macd < current_signal and prev_macd >= prev_signal
        
        return {
            "macd": round(current_macd, 2),
            "signal": round(current_signal, 2),
            "histogram": round(current_hist, 2),
            "golden_cross": golden_cross,
            "death_cross": death_cross,
            "signal": "bullish" if current_macd > current_signal else "bearish"
        }
    
    def calculate_kdj(self, n: int = 9, m1: int = 3, m2: int = 3) -> Dict:
        """计算KDJ"""
        if self.df is None or len(self.df) < n:
            return {}
            
        low_n = self.df['最低'].rolling(window=n).min()
        high_n = self.df['最高'].rolling(window=n).max()
        
        rsv = (self.df['收盘'] - low_n) / (high_n - low_n) * 100
        k = rsv.ewm(com=m1-1, adjust=False).mean()
        d = k.ewm(com=m2-1, adjust=False).mean()
        j = 3 * k - 2 * d
        
        current_k = k.iloc[-1]
        current_d = d.iloc[-1]
        current_j = j.iloc[-1]
        
        return {
            "k": round(current_k, 2),
            "d": round(current_d, 2),
            "j": round(current_j, 2),
            "signal": "overbought" if current_k > 80 else "oversold" if current_k < 20 else "neutral"
        }
    
    def calculate_rsi(self, period: int = 14) -> Dict:
        """计算RSI"""
        if self.df is None or len(self.df) < period:
            return {}
            
        delta = self.df['收盘'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        current_rsi = rsi.iloc[-1]
        
        return {
            "rsi": round(current_rsi, 2),
            "signal": "overbought" if current_rsi > 70 else "oversold" if current_rsi < 30 else "neutral"
        }
    
    def calculate_boll(self, period: int = 20, std_dev: int = 2) -> Dict:
        """计算布林带"""
        if self.df is None or len(self.df) < period:
            return {}
            
        middle = self.df['收盘'].rolling(window=period).mean()
        std = self.df['收盘'].rolling(window=period).std()
        
        upper = middle + (std * std_dev)
        lower = middle - (std * std_dev)
        
        current_close = self.df['收盘'].iloc[-1]
        current_upper = upper.iloc[-1]
        current_middle = middle.iloc[-1]
        current_lower = lower.iloc[-1]
        
        # 计算价格位置
        if current_close > current_upper:
            position = "above_upper"
        elif current_close < current_lower:
            position = "below_lower"
        else:
            position = "middle"
            
        return {
            "upper": round(current_upper, 2),
            "middle": round(current_middle, 2),
            "lower": round(current_lower, 2),
            "position": position,
            "bandwidth": round((current_upper - current_lower) / current_middle * 100, 2)
        }
    
    def calculate_cci(self, period: int = 20) -> Dict:
        """计算CCI"""
        if self.df is None or len(self.df) < period:
            return {}
            
        tp = (self.df['最高'] + self.df['最低'] + self.df['收盘']) / 3
        sma = tp.rolling(window=period).mean()
        mad = tp.rolling(window=period).apply(lambda x: np.abs(x - x.mean()).mean())
        
        cci = (tp - sma) / (0.015 * mad)
        
        current_cci = cci.iloc[-1]
        
        return {
            "cci": round(current_cci, 2),
            "signal": "overbought" if current_cci > 100 else "oversold" if current_cci < -100 else "neutral"
        }
    
    # ==================== 综合分析 ====================
    
    def full_analysis(self, symbol: str) -> Dict:
        """完整技术分析"""
        self.get_stock_data(symbol)
        
        if self.df is None or len(self.df) < 30:
            return {"error": "数据获取失败或数据不足"}
        
        # 计算所有指标
        ma_dict = self.calculate_ma()
        ma_sig = self.ma_signals()
        patterns = self.candlestick_patterns()
        macd = self.calculate_macd()
        kdj = self.calculate_kdj()
        rsi = self.calculate_rsi()
        boll = self.calculate_boll()
        cci = self.calculate_cci()
        
        # 综合评分
        score = 0
        bullish_count = 0
        bearish_count = 0
        
        # 均线信号
        if ma_sig.get("golden_cross"):
            score += 2
            bullish_count += 1
        if ma_sig.get("bullish_arrangement"):
            score += 3
            bullish_count += 1
            
        # MACD信号
        if macd.get("golden_cross"):
            score += 2
            bullish_count += 1
        if macd.get("death_cross"):
            score -= 2
            bearish_count += 1
            
        # KDJ信号
        if kdj.get("signal") == "oversold":
            score += 1
            bullish_count += 1
        elif kdj.get("signal") == "overbought":
            score -= 1
            bearish_count += 1
            
        # RSI信号
        if rsi.get("signal") == "oversold":
            score += 1
            bullish_count += 1
        elif rsi.get("signal") == "overbought":
            score -= 1
            bearish_count += 1
            
        # K线形态
        for p in patterns:
            if p.get("signal") == "bullish":
                score += 1
                bullish_count += 1
            elif p.get("signal") == "bearish":
                score -= 1
                bearish_count += 1
        
        # 总体判断
        if score >= 3:
            overall = "强烈看涨"
        elif score >= 1:
            overall = "谨慎看涨"
        elif score >= -1:
            overall = "中性"
        elif score >= -3:
            overall = "谨慎看跌"
        else:
            overall = "强烈看跌"
        
        return {
            "symbol": symbol,
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "close": round(self.df['收盘'].iloc[-1], 2),
            "ma": ma_dict,
            "ma_signals": ma_sig,
            "patterns": patterns,
            "macd": macd,
            "kdj": kdj,
            "rsi": rsi,
            "boll": boll,
            "cci": cci,
            "score": score,
            "bullish_count": bullish_count,
            "bearish_count": bearish_count,
            "overall": overall,
            "summary": self._generate_summary(score, bullish_count, bearish_count)
        }
    
    def _generate_summary(self, score: int, bullish: int, bearish: int) -> str:
        """生成分析总结"""
        if score >= 3:
            return f"技术面强烈看涨！均线多头排列，MACD金叉，{bullish}个看涨信号vs{bearish}个看跌信号，后市有望继续上涨。"
        elif score >= 1:
            return f"技术面谨慎看涨。{bullish}个看涨信号，{bearish}个看跌信号，建议关注均线支撑位。"
        elif score >= -1:
            return f"技术面中性。涨跌信号平衡({bullish} vs {bearish})，建议观望或轻仓操作。"
        elif score >= -3:
            return f"技术面谨慎看跌。{bearish}个看跌信号，注意控制风险。"
        else:
            return f"技术面强烈看跌！均线空头排列，{bearish}个看跌信号vs{bullish}个看涨信号，建议观望或做空。"


# 测试代码
if __name__ == "__main__":
    analyzer = TechnicalAnalyzer()
    result = analyzer.full_analysis("600519")  # 贵州茅台
    print(result)
