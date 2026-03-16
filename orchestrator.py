#!/usr/bin/env python3
"""
Financial Teams Orchestrator - 金融AI团队协调器
基于Financial CoT思维链的多Agent协作框架
"""

from typing import Dict, List, Optional
from datetime import datetime
import json

# 导入各分析模块
from technical_analyzer import TechnicalAnalyzer
from financial_report_analyzer import FinancialReportAnalyzer
from quant_factor import QuantFactorEngine
from chan_analyzer import ChanAnalyzer


class FinancialTeamsOrchestrator:
    """
    金融AI团队协调器
    
    核心思想：让AI分步推理金融问题，就像人类投顾一样思考
    """
    
    def __init__(self):
        self.agents = {
            'technical': TechnicalAnalyzer(),
            'financial_report': FinancialReportAnalyzer(),
            'quant_factor': QuantFactorEngine(),
            'chan': ChanAnalyzer()
        }
        
        # CoT思维链模板
        self.cot_template = """
你是一个专业的金融投顾团队，请按以下步骤分析：

## 步骤1：获取基本信息
- 股票代码：{symbol}
- 分析目的：{purpose}

## 步骤2：技术面分析
{technical_analysis}

## 步骤3：基本面分析
{financial_analysis}

## 步骤4：量化筛选
{quant_analysis}

## 步骤5：特殊理论分析
{chan_analysis}

## 步骤6：综合结论
基于以上分析，给出：
1. 整体评分（0-100）
2. 投资建议（买入/持有/卖出/观望）
3. 风险提示
4. 目标价位
"""
    
    def analyze_stock(self, symbol: str, purpose: str = "投资分析") -> Dict:
        """
        综合分析一只股票
        
        使用CoT思维链，分步推理
        """
        print(f"\n{'='*50}")
        print(f"开始分析: {symbol}")
        print(f"{'='*50}")
        
        # ========== 步骤1: 获取基本信息 ==========
        print("\n[步骤1] 获取基本信息...")
        
        # ========== 步骤2: 技术面分析 ==========
        print("[步骤2] 进行技术分析...")
        try:
            technical_result = self.agents['technical'].full_analysis(symbol)
            tech_summary = technical_result.get('summary', '技术分析完成')
            print(f"  技术面: {tech_summary}")
        except Exception as e:
            print(f"  技术分析失败: {e}")
            technical_result = {}
            tech_summary = "技术分析暂不可用"
        
        # ========== 步骤3: 基本面分析 ==========
        print("[步骤3] 进行财报分析...")
        try:
            financial_result = self.agents['financial_report'].analyze(symbol)
            fin_summary = financial_result.get('summary', '财报分析完成')
            print(f"  基本面: {fin_summary}")
        except Exception as e:
            print(f"  财报分析失败: {e}")
            financial_result = {}
            fin_summary = "基本面分析暂不可用"
        
        # ========== 步骤4: 量化筛选 ==========
        print("[步骤4] 量化因子分析...")
        try:
            quant_result = self.agents['quant_factor'].smart_select("growth")
            quant_summary = f"选出{len(quant_result.get('stocks', []))}只成长股"
            print(f"  量化: {quant_summary}")
        except Exception as e:
            print(f"  量化分析失败: {e}")
            quant_summary = "量化分析暂不可用"
        
        # ========== 步骤5: 缠论分析 ==========
        print("[步骤5] 缠论分析...")
        try:
            chan_result = self.agents['chan'].find_signals()
            chan_summary = chan_result.get('summary', '缠论分析完成')
            print(f"  缠论: {chan_summary}")
        except Exception as e:
            print(f"  缠论分析失败: {e}")
            chan_summary = "缠论分析暂不可用"
        
        # ========== 步骤6: 综合结论 ==========
        print("\n[步骤6] 生成综合结论...")
        
        # 计算综合评分
        score = self._calculate_composite_score(
            technical_result,
            financial_result,
            quant_result
        )
        
        # 生成投资建议
        recommendation = self._generate_recommendation(score)
        
        # 风险评估
        risks = self._assess_risks(technical_result, financial_result)
        
        # 目标价
        target_price = self._calculate_target_price(technical_result, financial_result)
        
        result = {
            'symbol': symbol,
            'purpose': purpose,
            'analysis_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            
            # 各维度分析结果
            'technical': technical_result,
            'financial': financial_result,
            'quant': quant_result,
            'chan': chan_result if 'chan_result' in dir() else {},
            
            # 综合结论
            'composite_score': score,
            'recommendation': recommendation,
            'risks': risks,
            'target_price': target_price,
            
            # 思维链总结
            'cot_summary': self._generate_cot_summary(
                tech_summary, fin_summary, chan_summary, 
                score, recommendation
            )
        }
        
        print(f"\n{'='*50}")
        print(f"分析完成!")
        print(f"综合评分: {score}")
        print(f"投资建议: {recommendation}")
        print(f"{'='*50}")
        
        return result
    
    def _calculate_composite_score(self, tech, financial, quant) -> int:
        """计算综合评分"""
        score = 50  # 基础分
        
        # 技术面评分
        tech_score = tech.get('score', 0) if tech else 0
        score += int(tech_score * 0.25)  # 25%权重
        
        # 基本面评分
        fin_score = financial.get('score', 50) if financial else 50
        score += int(fin_score * 0.35)  # 35%权重
        
        # 量化筛选
        stocks = quant.get('stocks', []) if quant else []
        if symbol in [s.get('code', '') for s in stocks[:10]]:
            score += 10  # 入选量化选股
        
        # 缠论信号
        if tech.get('overall', '') in ['强烈看涨', '谨慎看涨']:
            score += 5
        
        return max(0, min(100, score))
    
    def _generate_recommendation(self, score: int) -> str:
        """生成投资建议"""
        if score >= 80:
            return "强烈推荐"
        elif score >= 65:
            return "推荐买入"
        elif score >= 50:
            return "持有观望"
        elif score >= 35:
            return "谨慎持有"
        else:
            return "建议回避"
    
    def _assess_risks(self, tech, financial) -> List[str]:
        """评估风险"""
        risks = []
        
        if tech:
            if tech.get('overall', '') in ['谨慎看跌', '强烈看跌']:
                risks.append("技术面承压")
                
        if financial:
            fin_risks = financial.get('risks', [])
            risks.extend(fin_risks[:2])
        
        if not risks:
            risks.append("无明显风险提示")
            
        return risks
    
    def _calculate_target_price(self, tech, financial) -> Optional[float]:
        """计算目标价"""
        try:
            current = tech.get('close', 0) if tech else 0
            if current > 0:
                # 基于技术面和基本面给出一个乐观目标价
                return round(current * 1.2, 2)  # 20%上涨空间
        except:
            pass
        return None
    
    def _generate_cot_summary(self, tech, fin, chan, score, rec) -> str:
        """生成思维链总结"""
        return f"""
## 综合分析报告

### 技术面
{tech}

### 基本面
{fin}

### 缠论分析
{chan}

### 综合评分
- 评分：{score}/100
- 建议：{rec}

### 分析流程（Financial CoT）
1. 获取实时行情和技术指标
2. 分析财务报表和估值水平
3. 进行多因子量化筛选
4. 运用缠论判断走势结构
5. 综合所有信息给出结论

---
*本报告由Financial Teams AI团队生成，仅供参考，不构成投资建议*
"""
    
    def batch_analyze(self, symbols: List[str]) -> List[Dict]:
        """批量分析多只股票"""
        results = []
        for symbol in symbols:
            try:
                result = self.analyze_stock(symbol)
                results.append(result)
            except Exception as e:
                print(f"分析{symbol}失败: {e}")
                results.append({'symbol': symbol, 'error': str(e)})
        return results


# ==================== 主程序 ====================

if __name__ == "__main__":
    # 创建协调器
    orchestrator = FinancialTeamsOrchestrator()
    
    # 分析贵州茅台
    result = orchestrator.analyze_stock("600519", purpose="投资分析")
    
    # 打印结果
    print("\n" + "="*50)
    print("最终报告:")
    print("="*50)
    print(result['cot_summary'])
