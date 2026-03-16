#!/usr/bin/env python3
"""
Quant Factor Agent - 量化因子核心模块
多因子选股、因子回测、策略优化
"""

import akshare as ak
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class QuantFactorEngine:
    """量化因子引擎"""
    
    def __init__(self):
        self.factors = {}
        self.stock_pool = []
        
    # ==================== 因子计算 ====================
    
    def get_stock_list(self, market: str = "沪深A股") -> List[str]:
        """获取股票列表"""
        try:
            df = ak.stock_zh_a_spot_em()
            self.stock_pool = df['代码'].tolist()[:100]  # 取前100只
            return self.stock_pool
        except Exception as e:
            print(f"获取股票列表失败: {e}")
            return []
    
    def calculate_pe(self, symbol: str) -> float:
        """计算市盈率"""
        try:
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == symbol]
            if stock.empty:
                return 0
            pe = stock.iloc[0]['市盈率-动态']
            return float(pe) if pd.notna(pe) and pe > 0 else 0
        except:
            return 0
    
    def calculate_pb(self, symbol: str) -> float:
        """计算市净率"""
        try:
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == symbol]
            if stock.empty:
                return 0
            pb = stock.iloc[0]['市净率']
            return float(pb) if pd.notna(pb) and pb > 0 else 0
        except:
            return 0
    
    def calculate_market_cap(self, symbol: str) -> float:
        """计算总市值（亿）"""
        try:
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == symbol]
            if stock.empty:
                return 0
            cap = stock.iloc[0]['总市值']
            return float(cap) if pd.notna(cap) else 0
        except:
            return 0
    
    def calculate_roe(self, symbol: str) -> float:
        """获取ROE"""
        try:
            df = ak.stock_financial_analysis_indicator(symbol=symbol)
            if df.empty:
                return 0
            roe = df.iloc[0]['净资产收益率']
            return float(roe) if pd.notna(roe) else 0
        except:
            return 0
    
    def calculate_growth(self, symbol: str) -> float:
        """获取净利润增速"""
        try:
            df = ak.stock_financial_abstract_ths(symbol=symbol, indicator="按报告期")
            if df.empty:
                return 0
            growth = df.iloc[0]['净利润同比增长']
            if isinstance(growth, str):
                growth = growth.replace('%', '')
            return float(growth) if pd.notna(growth) else 0
        except:
            return 0
    
    def calculate_momentum(self, symbol: str, days: int = 20) -> float:
        """计算动量因子（涨跌幅）"""
        try:
            df = ak.stock_zh_a_hist(symbol=symbol, 
                                   start_date=(datetime.now() - timedelta(days=days+10)).strftime("%Y%m%d"),
                                   end_date=datetime.now().strftime("%Y%m%d"),
                                   adjust="qfq")
            if df.empty or len(df) < days:
                return 0
            price_start = df.iloc[0]['收盘']
            price_end = df.iloc[-1]['收盘']
            return ((price_end - price_start) / price_start) * 100
        except:
            return 0
    
    # ==================== 多因子选股 ====================
    
    def factor_screening(self, 
                        min_pe: float = 0, max_pe: float = 50,
                        min_roe: float = 0, 
                        min_growth: float = -100,
                        max_market_cap: float = 10000,
                        min_momentum: float = -100) -> List[Dict]:
        """多因子筛选"""
        if not self.stock_pool:
            self.get_stock_list()
        
        results = []
        
        for symbol in self.stock_pool[:50]:  # 筛选前50只
            try:
                pe = self.calculate_pe(symbol)
                pb = self.calculate_pb(symbol)
                cap = self.calculate_market_cap(symbol)
                roe = self.calculate_roe(symbol)
                growth = self.calculate_growth(symbol)
                momentum = self.calculate_momentum(symbol, 20)
                
                # 筛选条件
                if (pe >= min_pe and pe <= max_pe and pe > 0 and
                    roe >= min_roe and
                    growth >= min_growth and
                    cap <= max_market_cap and
                    momentum >= min_momentum):
                    
                    results.append({
                        'code': symbol,
                        'pe': round(pe, 2),
                        'pb': round(pb, 2),
                        'market_cap': round(cap, 2),
                        'roe': round(roe, 2),
                        'growth': round(growth, 2),
                        'momentum': round(momentum, 2),
                        'score': self._calculate_score(pe, roe, growth, momentum)
                    })
            except:
                continue
        
        # 按综合评分排序
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results[:20]  # 返回前20只
    
    def _calculate_score(self, pe, roe, growth, momentum):
        """计算综合评分"""
        score = 0
        
        # ROE评分（越高越好）
        if roe > 20: score += 30
        elif roe > 15: score += 20
        elif roe > 10: score += 10
        
        # 成长性评分
        if growth > 50: score += 25
        elif growth > 20: score += 20
        elif growth > 0: score += 10
        elif growth > -10: score += 5
        
        # 估值评分（PE越低越好）
        if 0 < pe < 15: score += 25
        elif 15 <= pe < 25: score += 15
        elif 25 <= pe < 35: score += 5
        
        # 动量评分
        if momentum > 10: score += 20
        elif momentum > 5: score += 15
        elif momentum > 0: score += 10
        elif momentum > -5: score += 5
        
        return score
    
    # ==================== 行业选股 ====================
    
    def get_industry_stocks(self, industry: str) -> List[str]:
        """获取行业成分股"""
        try:
            df = ak.stock_board_industry_name_em()
            board = df[df['板块名称'] == industry]
            if board.empty:
                return []
            # 获取行业详情
            code = board.iloc[0]['板块代码']
            df_stocks = ak.stock_board_industry_cons_em(symbol=code)
            return df_stocks['代码'].tolist()[:30]
        except Exception as e:
            print(f"获取行业股票失败: {e}")
            return []
    
    def industry_factor_screening(self, industry: str) -> List[Dict]:
        """行业多因子选股"""
        stocks = self.get_industry_stocks(industry)
        
        results = []
        for symbol in stocks[:30]:
            try:
                pe = self.calculate_pe(symbol)
                roe = self.calculate_roe(symbol)
                growth = self.calculate_growth(symbol)
                momentum = self.calculate_momentum(symbol, 20)
                
                results.append({
                    'code': symbol,
                    'pe': round(pe, 2) if pe > 0 else 999,
                    'roe': round(roe, 2),
                    'growth': round(growth, 2),
                    'momentum': round(momentum, 2),
                    'score': self._calculate_score(pe, roe, growth, momentum)
                })
            except:
                continue
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:10]
    
    # ==================== 策略回测 ====================
    
    def backtest(self, symbols: List[str], days: int = 60) -> Dict:
        """简单回测"""
        results = []
        
        for symbol in symbols[:10]:
            try:
                df = ak.stock_zh_a_hist(symbol=symbol,
                                       start_date=(datetime.now() - timedelta(days=days+10)).strftime("%Y%m%d"),
                                       end_date=datetime.now().strftime("%Y%m%d"),
                                       adjust="qfq")
                if len(df) < days:
                    continue
                    
                # 买入持有策略
                price_start = df.iloc[10]['收盘']  # 忽略前10天
                price_end = df.iloc[-1]['收盘']
                returns = (price_end - price_start) / price_start * 100
                
                # 计算最大回撤
                df_subset = df.iloc[10:]
                rolling_max = df_subset['收盘'].cummax()
                drawdown = (df_subset['收盘'] - rolling_max) / rolling_max * 100
                max_drawdown = drawdown.min()
                
                results.append({
                    'symbol': symbol,
                    'returns': round(returns, 2),
                    'max_drawdown': round(max_drawdown, 2),
                    'days': days
                })
            except:
                continue
        
        if not results:
            return {"error": "回测数据不足"}
        
        # 计算组合收益
        avg_return = np.mean([r['returns'] for r in results])
        
        return {
            'symbols_tested': len(results),
            'avg_return': round(avg_return, 2),
            'best_return': max([r['returns'] for r in results]),
            'worst_return': min([r['returns'] for r in results]),
            'results': sorted(results, key=lambda x: x['returns'], reverse=True)[:5],
            'conclusion': "策略盈利" if avg_return > 0 else "策略亏损"
        }
    
    # ==================== 智能选股 ====================
    
    def smart_select(self, strategy: str = "growth") -> Dict:
        """智能选股策略"""
        if strategy == "growth":
            # 成长股策略
            return {
                'strategy': '成长股策略',
                'stocks': self.factor_screening(min_roe=10, min_growth=20),
                'logic': '高ROE + 高增长'
            }
        elif strategy == "value":
            # 价值股策略
            return {
                'strategy': '价值股策略',
                'stocks': self.factor_screening(min_pe=0, max_pe=20, min_roe=10),
                'logic': '低PE + 高ROE'
            }
        elif strategy == "momentum":
            # 动量策略
            return {
                'strategy': '动量策略',
                'stocks': self.factor_screening(min_momentum=5),
                'logic': '强势股 + 趋势向上'
            }
        elif strategy == "quality":
            # 质量策略
            return {
                'strategy': '质量策略',
                'stocks': self.factor_screening(min_roe=15, max_market_cap=5000),
                'logic': '高ROE + 中小市值'
            }
        else:
            # 综合策略
            return {
                'strategy': '综合策略',
                'stocks': self.factor_screening(min_roe=5, min_growth=0),
                'logic': '综合评分最优'
            }


# 测试代码
if __name__ == "__main__":
    engine = QuantFactorEngine()
    
    # 成长股选股
    result = engine.smart_select("growth")
    print("成长股策略:")
    print(result)
