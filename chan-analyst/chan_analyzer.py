#!/usr/bin/env python3
"""
Chan Theory Analyst - 缠论分析核心模块
基于缠中说禅理论进行走势分析
"""

import akshare as ak
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class ChanAnalyzer:
    """缠论分析器"""
    
    def __init__(self):
        self.df = None
        self.symbol = None
        
    def get_data(self, symbol: str, days: int = 250) -> pd.DataFrame:
        """获取K线数据"""
        self.symbol = symbol
        
        if "." not in symbol:
            symbol = f"{symbol}.SH"
            
        try:
            df = ak.stock_zh_a_hist(
                symbol=symbol.replace(".SH", ""),
                start_date=(datetime.now() - timedelta(days=days+30)).strftime("%Y%m%d"),
                end_date=datetime.now().strftime("%Y%m%d"),
                adjust="qfq"
            )
            df = df.sort_values('日期')
            df.reset_index(drop=True, inplace=True)
            self.df = df
            return df
        except Exception as e:
            print(f"获取数据失败: {e}")
            return pd.DataFrame()
    
    # ==================== 分型识别 ====================
    
    def find_fractals(self) -> List[Dict]:
        """识别分型（顶分型/底分型）"""
        if self.df is None or len(self.df) < 5:
            return []
        
        fractals = []
        
        for i in range(2, len(self.df) - 2):
            left = self.df.iloc[i-2:i+1]
            center = self.df.iloc[i-1:i+2]
            right = self.df.iloc[i:i+3]
            
            # 顶分型：中间K线最高
            if (center['最高'].max() == self.df.iloc[i]['最高'] and
                self.df.iloc[i]['最高'] > left['最高'].max() and
                self.df.iloc[i]['最高'] > right['最高'].max()):
                
                # 判断是否连续
                if len(fractals) > 0 and fractals[-1]['type'] == '顶分型':
                    if fractals[-1]['index'] == i - 1:
                        continue
                        
                fractals.append({
                    'index': i,
                    'date': str(self.df.iloc[i]['日期']),
                    'type': '顶分型',
                    'price': self.df.iloc[i]['最高'],
                    'strength': self._fractal_strength(i)
                })
            
            # 底分型：中间K线最低
            elif (center['最低'].min() == self.df.iloc[i]['最低'] and
                  self.df.iloc[i]['最低'] < left['最低'].min() and
                  self.df.iloc[i]['最低'] < right['最低'].min()):
                  
                if len(fractals) > 0 and fractals[-1]['type'] == '底分型':
                    if fractals[-1]['index'] == i - 1:
                        continue
                        
                fractals.append({
                    'index': i,
                    'date': str(self.df.iloc[i]['日期']),
                    'type': '底分型',
                    'price': self.df.iloc[i]['最低'],
                    'strength': self._fractal_strength(i)
                })
        
        return fractals
    
    def _fractal_strength(self, i: int) -> str:
        """判断分型强度"""
        if i < 2 or i > len(self.df) - 3:
            return "弱"
            
        left_range = self.df.iloc[i-2:i+1]['最高'].max() - self.df.iloc[i-2:i+1]['最低'].min()
        right_range = self.df.iloc[i:i+3]['最高'].max() - self.df.iloc[i:i+3]['最低'].min()
        
        if left_range > 0 and right_range > 0:
            if left_range / right_range > 1.5:
                return "强"
            elif right_range / left_range > 1.5:
                return "弱"
        
        return "中"
    
    # ==================== 笔的划分 ====================
    
    def find_pen(self, min_bars: int = 5) -> List[Dict]:
        """识别笔"""
        fractals = self.find_fractals()
        
        if len(fractals) < 2:
            return []
        
        pens = []
        i = 0
        
        while i < len(fractals) - 1:
            top = fractals[i] if fractals[i]['type'] == '顶分型' else None
            bottom = None
            
            # 寻找匹配的底分型
            for j in range(i + 1, len(fractals)):
                if fractals[j]['type'] == '底分型':
                    bottom = fractals[j]
                    # 检查是否有足够的K线
                    if bottom['index'] - (top['index'] if top else 0) >= min_bars:
                        break
                    bottom = None
            
            if top and bottom:
                # 上涨笔
                pens.append({
                    'type': '上涨笔',
                    'start': top['date'],
                    'end': bottom['date'],
                    'start_price': top['price'],
                    'end_price': bottom['price'],
                    'range': round(bottom['price'] - top['price'], 2),
                    'bars': bottom['index'] - top['index']
                })
                i = fractals.index(bottom)
            
            # 寻找匹配的顶分型
            bottom = fractals[i] if fractals[i]['type'] == '底分型' else None
            top = None
            
            for j in range(i + 1, len(fractals)):
                if fractals[j]['type'] == '顶分型':
                    top = fractals[j]
                    if top['index'] - (bottom['index'] if bottom else 0) >= min_bars:
                        break
                    top = None
            
            if top and bottom:
                # 下跌笔
                pens.append({
                    'type': '下跌笔',
                    'start': bottom['date'],
                    'end': top['date'],
                    'start_price': bottom['price'],
                    'end_price': top['price'],
                    'range': round(bottom['price'] - top['price'], 2),
                    'bars': top['index'] - bottom['index']
                })
                i = fractals.index(top)
            else:
                i += 1
        
        return pens
    
    # ==================== 中枢识别 ====================
    
    def find_zhongshu(self) -> List[Dict]:
        """识别中枢"""
        pens = self.find_pen()
        
        if len(pens) < 3:
            return []
        
        zhongshu = []
        
        # 简化版：找出重叠的笔构建中枢
        for i in range(len(pens) - 2):
            pen1 = pens[i]
            pen2 = pens[i + 1]
            pen3 = pens[i + 2]
            
            # 判断方向是否相反且有重叠
            if (pen1['type'] != pen2['type'] and 
                pen2['type'] != pen3['type'] and
                pen1['type'] == pen3['type']):
                
                # 计算重叠区间
                if pen1['type'] == '上涨笔':
                    high = min(pen1['end_price'], pen2['start_price'])
                    low = max(pen1['end_price'], pen2['start_price'])
                    
                    if low < high:
                        zhongshu.append({
                            'type': '上涨中枢',
                            'high': round(high, 2),
                            'low': round(low, 2),
                            'range': round(high - low, 2),
                            'start': pen2['start'],
                            'end': pen2['end']
                        })
                else:
                    high = max(pen1['end_price'], pen2['start_price'])
                    low = min(pen1['end_price'], pen2['start_price'])
                    
                    if high > low:
                        zhongshu.append({
                            'type': '下跌中枢',
                            'high': round(high, 2),
                            'low': round(low, 2),
                            'range': round(high - low, 2),
                            'start': pen2['start'],
                            'end': pen2['end']
                        })
        
        return zhongshu
    
    # ==================== 背驰判断 ====================
    
    def find_beichi(self) -> List[Dict]:
        """判断背驰"""
        pens = self.find_pen()
        
        if len(pens) < 4:
            return []
        
        beichi = []
        
        for i in range(3, len(pens)):
            # 连续同方向的三笔
            if (pens[i-3]['type'] == pens[i-2]['type'] == pens[i-1]['type'] == pens[i]['type']):
                
                pen1_range = abs(pens[i-3]['range'])
                pen2_range = abs(pens[i-2]['range'])
                pen3_range = abs(pens[i-1]['range'])
                pen4_range = abs(pens[i]['range'])
                
                # 背驰：后一段力度小于前一段
                if pens[i]['type'] == '上涨笔':
                    if pen4_range < pen3_range and pen3_range < pen2_range:
                        beichi.append({
                            'type': '顶背驰',
                            'signal': '卖点',
                            'description': f'上涨力度衰竭，笔4({pen4_range:.2f}) < 笔3({pen3_range:.2f}) < 笔2({pen2_range:.2f})'
                        })
                else:
                    if pen4_range < pen3_range and pen3_range < pen2_range:
                        beichi.append({
                            'type': '底背驰',
                            'signal': '买点',
                            'description': f'下跌力度衰竭，笔4({pen4_range:.2f}) < 笔3({pen3_range:.2f}) < 笔2({pen2_range:.2f})'
                        })
        
        return beichi
    
    # ==================== 买卖点 ====================
    
    def find_signals(self) -> Dict:
        """综合买卖点信号"""
        fractals = self.find_fractals()
        pens = self.find_pen()
        zhongshu = self.find_zhongshu()
        beichi = self.find_beichi()
        
        signals = []
        
        # 基于背驰的买卖点
        for b in beichi:
            signals.append({
                'type': b['type'],
                'signal': b['signal'],
                'level': '一买' if '一' in b.get('description', '') else '二买',
                'description': b['description']
            })
        
        # 基于分型的买卖点（简化版）
        if len(fractals) >= 2:
            last = fractals[-1]
            second_last = fractals[-2]
            
            if last['type'] == '底分型':
                signals.append({
                    'type': '分型买点',
                    'signal': '买入',
                    'level': '激进',
                    'description': f"出现底分型，价位{last['price']}"
                })
            elif last['type'] == '顶分型':
                signals.append({
                    'type': '分型卖点',
                    'signal': '卖出',
                    'level': '激进',
                    'description': f"出现顶分型，价位{last['price']}"
                })
        
        # 当前趋势判断
        if len(pens) >= 2:
            last_pen = pens[-1]
            trend = "上涨趋势" if last_pen['type'] == '上涨笔' else "下跌趋势"
        else:
            trend = "盘整"
        
        return {
            'symbol': self.symbol,
            'analysis_date': datetime.now().strftime("%Y-%m-%d"),
            'trend': trend,
            'fractals_count': len(fractals),
            'pens_count': len(pens),
            'zhongshu_count': len(zhongshu),
            'signals': signals,
            'summary': self._generate_summary(trend, signals, beichi)
        }
    
    def _generate_summary(self, trend: str, signals: List, beichi: List) -> str:
        """生成分析总结"""
        parts = []
        
        parts.append(f"当前趋势：{trend}。")
        
        if beichi:
            parts.append(f"检测到{len(beichi)}个背驰信号，")
            for b in beichi:
                parts.append(f"{b['type']}({b['signal']})，")
        
        if signals:
            buy_signals = [s for s in signals if '买' in s.get('signal', '')]
            sell_signals = [s for s in signals if '卖' in s.get('signal', '')]
            
            if buy_signals:
                parts.append(f"存在{len(buy_signals)}个买入信号，建议关注。")
            elif sell_signals:
                parts.append(f"存在{len(sell_signals)}个卖出信号，注意风险。")
            else:
                parts.append("建议观望。")
        else:
            parts.append("暂无明确信号，建议观望。")
        
        return "".join(parts)
    
    # ==================== 完整分析 ====================
    
    def full_analysis(self, symbol: str) -> Dict:
        """完整缠论分析"""
        self.get_data(symbol)
        
        if self.df is None or len(self.df) < 30:
            return {"error": "数据不足"}
        
        fractals = self.find_fractals()
        pens = self.find_pen()
        zhongshu = self.find_zhongshu()
        beichi = self.find_beichi()
        signals = self.find_signals()
        
        return {
            'symbol': symbol,
            'analysis_date': datetime.now().strftime("%Y-%m-%d"),
            'fractals': fractals[-10:] if fractals else [],  # 最近10个分型
            'pens': pens[-5:] if pens else [],  # 最近5笔
            'zhongshu': zhongshu[-3:] if zhongshu else [],  # 最近3个中枢
            'beichi': beichi,
            'signals': signals
        }


# 测试代码
if __name__ == "__main__":
    chan = ChanAnalyzer()
    result = chan.full_analysis("000001")  # 平安银行
    print(result)
