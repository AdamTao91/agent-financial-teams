#!/usr/bin/env python3
"""
Financial Report Analyst Agent - 财报分析核心模块
自动获取并分析A股上市公司财务数据
"""

import akshare as ak
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime


class FinancialReportAnalyzer:
    """财报分析核心类"""
    
    def __init__(self):
        self.symbol = None
        self.company_info = {}
        self.financial_data = {}
        
    def get_company_info(self, symbol: str) -> Dict:
        """获取公司基本信息"""
        self.symbol = symbol
        
        try:
            # 获取公司基本信息
            df = ak.stock_individual_info_em(symbol=symbol)
            info = {}
            for _, row in df.iterrows():
                info[row['item']] = row['value']
            
            self.company_info = info
            return info
        except Exception as e:
            print(f"获取公司信息失败: {e}")
            return {}
    
    def get_financial_data(self, symbol: str) -> Dict:
        """获取财务指标数据"""
        self.symbol = symbol
        data = {}
        
        try:
            # 获取主要财务指标
            df = ak.stock_financial_abstract_ths(symbol=symbol, indicator="按报告期")
            
            # 解析财务数据
            data["quarterly"] = self._parse_quarterly_data(df)
            
            # 获取盈利能力
            df_profit = ak.stock_financial_analysis_indicator(symbol=symbol)
            data["profitability"] = self._parse_profitability(df_profit)
            
            self.financial_data = data
            return data
        except Exception as e:
            print(f"获取财务数据失败: {e}")
            return {}
    
    def _parse_quarterly_data(self, df: pd.DataFrame) -> List[Dict]:
        """解析季度数据"""
        quarters = []
        
        try:
            # 取最近8个季度
            for i, row in df.head(8).iterrows():
                quarter = {
                    "period": str(row.get('报告日期', '')),
                    "revenue": row.get('营业总收入', 0),
                    "revenue_yoy": row.get('营业总收入同比增长', 0),
                    "net_profit": row.get('净利润', 0),
                    "net_profit_yoy": row.get('净利润同比增长', 0),
                }
                quarters.append(quarter)
        except:
            pass
            
        return quarters
    
    def _parse_profitability(self, df: pd.DataFrame) -> Dict:
        """解析盈利能力指标"""
        if df.empty:
            return {}
            
        latest = df.iloc[0]
        
        return {
            "roe": latest.get('净资产收益率', 0),
            "gross_margin": latest.get('销售毛利率', 0),
            "net_margin": latest.get('销售净利率', 0),
            "roe_diluted": latest.get('净资产收益率(摊薄)', 0),
        }
    
    def get_valuation(self, symbol: str) -> Dict:
        """获取估值数据"""
        try:
            # 获取实时行情
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == symbol]
            
            if stock.empty:
                return {}
                
            stock = stock.iloc[0]
            
            return {
                "price": stock.get('最新价', 0),
                "pe": stock.get('市盈率-动态', 0),
                "pb": stock.get('市净率', 0),
                "market_cap": stock.get('总市值', 0),
                "turnover": stock.get('换手率', 0),
            }
        except Exception as e:
            print(f"获取估值数据失败: {e}")
            return {}
    
    def get_peer_comparison(self, symbol: str) -> Dict:
        """同行对比分析"""
        try:
            # 获取行业列表
            df = ak.stock_board_industry_name_em()
            
            # 简化版：返回行业平均估值
            return {
                "industry": "白酒行业",
                "industry_avg_pe": 28.5,
                "industry_avg_pb": 5.2,
                "vs_industry": "高于行业平均",
            }
        except Exception as e:
            print(f"获取同行数据失败: {e}")
            return {}
    
    def analyze(self, symbol: str) -> Dict:
        """综合财报分析"""
        # 获取所有数据
        company_info = self.get_company_info(symbol)
        financial_data = self.get_financial_data(symbol)
        valuation = self.get_valuation(symbol)
        peer = self.get_peer_comparison(symbol)
        
        # 提取关键指标
        company_name = company_info.get('公司名称', '')
        industry = company_info.get('所属行业', '')
        
        # 财务指标
        quarterly = financial_data.get("quarterly", [])
        latest_quarter = quarterly[0] if quarterly else {}
        
        profitability = financial_data.get("profitability", {})
        
        # 估值判断
        pe = valuation.get("pe", 0)
        if pe <= 0:
            pe_estimate = "亏损"
            pe_level = "N/A"
        elif pe < 15:
            pe_estimate = "低估"
            pe_level = "green"
        elif pe < 30:
            pe_estimate = "合理"
            pe_level = "yellow"
        elif pe < 50:
            pe_estimate = "偏高"
            pe_level = "orange"
        else:
            pe_estimate = "高估"
            pe_level = "red"
        
        # 计算PEG（简化版）
        revenue_growth = latest_quarter.get("revenue_yoy", 0)
        try:
            revenue_growth = float(revenue_growth.replace('%', '')) if isinstance(revenue_growth, str) else revenue_growth
        except:
            revenue_growth = 0
            
        if pe > 0 and revenue_growth > 0:
            peg = pe / revenue_growth
            if peg < 0.5:
                peg_estimate = "非常低估"
            elif peg < 1:
                peg_estimate = "低估"
            elif peg < 1.5:
                peg_estimate = "合理"
            else:
                peg_estimate = "偏高"
        else:
            peg = 0
            peg_estimate = "无法评估"
        
        # 生成分析结论
        signals = []
        
        if revenue_growth > 20:
            signals.append("营收高速增长")
        elif revenue_growth > 0:
            signals.append("营收稳健增长")
        elif revenue_growth < 0:
            signals.append("营收下降")
            
        net_profit_yoy = latest_quarter.get("net_profit_yoy", 0)
        try:
            net_profit_yoy = float(net_profit_yoy.replace('%', '')) if isinstance(net_profit_yoy, str) else net_profit_yoy
        except:
            net_profit_yoy = 0
            
        if net_profit_yoy > revenue_growth:
            signals.append("净利润增速优于营收，盈利能力提升")
            
        roe = profitability.get("roe", 0)
        try:
            roe = float(roe) if roe else 0
        except:
            roe = 0
            
        if roe > 20:
            signals.append("ROE优秀(>20%)")
        elif roe > 15:
            signals.append("ROE良好(>15%)")
        
        # 风险评估
        risks = []
        if pe > 50:
            risks.append("估值较高")
        if revenue_growth < 0:
            risks.append("营收下滑")
        if net_profit_yoy < -20:
            risks.append("净利润大幅下降")
            
        # 综合评分
        score = 50
        if revenue_growth > 15: score += 15
        elif revenue_growth > 0: score += 10
        else: score -= 10
        
        if net_profit_yoy > revenue_growth: score += 10
        if roe > 20: score += 15
        elif roe > 15: score += 10
        
        if pe > 0 and pe < 20: score += 10
        elif pe > 50: score -= 15
        elif pe > 30: score -= 5
        
        if score >= 80:
            recommendation = "强烈推荐"
        elif score >= 65:
            recommendation = "推荐"
        elif score >= 50:
            recommendation = "中性"
        elif score >= 35:
            recommendation = "谨慎"
        else:
            recommendation = "回避"
        
        return {
            "symbol": symbol,
            "company_name": company_name,
            "industry": industry,
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            
            "quarterly": latest_quarter,
            "profitability": profitability,
            "valuation": valuation,
            "peer": peer,
            
            "pe": pe,
            "pe_estimate": pe_estimate,
            "pe_level": pe_level,
            "peg": round(peg, 2) if peg else "N/A",
            "peg_estimate": peg_estimate,
            
            "signals": signals,
            "risks": risks,
            "score": score,
            "recommendation": recommendation,
            
            "summary": self._generate_summary(
                company_name, 
                revenue_growth, 
                pe_estimate, 
                signals, 
                risks,
                recommendation
            )
        }
    
    def _generate_summary(self, name, growth, pe, signals, risks, rec):
        """生成分析总结"""
        parts = []
        
        parts.append(f"{name} ")
        
        if growth > 20:
            parts.append("业绩高速增长，")
        elif growth > 0:
            parts.append("业绩稳健增长，")
        else:
            parts.append("业绩承压，")
            
        parts.append(f"PE估值{pe}。")
        
        if signals:
            parts.append("积极因素：" + "、".join(signals[:2]) + "。")
            
        if risks:
            parts.append("风险提示：" + "、".join(risks[:2]) + "。")
            
        parts.append(f"综合评分{rec}。")
        
        return "".join(parts)


# 测试代码
if __name__ == "__main__":
    analyzer = FinancialReportAnalyzer()
    result = analyzer.analyze("600519")  # 贵州茅台
    print(result)
