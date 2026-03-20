#!/usr/bin/env python3
"""
Financial Teams - 使用示例集锦

包含各种常见使用场景的代码示例
"""

# ==================== 基础示例 ====================

# 示例1: 快速持仓诊断
def example_portfolio_diagnosis():
    """快速诊断持仓"""
    from investment_advisor import Advisor
    
    advisor = Advisor()
    result = advisor.diagnose(
        code="588830",           # 基金代码
        position=200000,        # 持仓金额20万
        holding_months=4        # 持有4个月
    )
    print(result)


# 示例2: 行业深度分析
def example_industry_analysis():
    """分析特定行业"""
    from industry_researcher import Researcher
    
    researcher = Researcher()
    report = researcher.analyze(
        industry="新能源车",
        depth="deep"             # deep 或 quick
    )
    print(report)


# 示例3: ETF智能推荐
def example_etf_recommendation():
    """根据风险偏好推荐ETF"""
    from wealth_advisor import WealthAdvisor
    
    advisor = WealthAdvisor()
    
    # 推荐稳健型ETF
    conservative = advisor.recommend_etf(risk_level="low")
    
    # 推荐平衡型ETF
    balanced = advisor.recommend_etf(risk_level="medium")
    
    # 推荐激进型ETF
    aggressive = advisor.recommend_etf(risk_level="high")
    
    return conservative, balanced, aggressive


# 示例4: 获取交易信号
def example_trading_signal():
    """获取买卖信号"""
    from business_opportunity_analyst import Analyst
    
    analyst = Analyst()
    signal = analyst.get_signal("588830")
    
    print(f"股票: {signal['code']}")
    print(f"信号: {signal['action']}")      # 买入/卖出/持有
    print(f"置信度: {signal['confidence']}%")
    print(f"目标价: {signal['target_price']}")
    print(f"止损价: {signal['stop_loss']}")


# 示例5: 风险监控
def example_risk_monitoring():
    """监控持仓风险"""
    from corporate_sentiment_analyst import Analyst
    
    analyst = Analyst()
    risks = analyst.monitor(["588830", "510300"])
    
    for risk in risks:
        print(f"股票: {risk['code']}")
        print(f"风险等级: {risk['level']}")  # low/medium/high
        print(f"风险描述: {risk['description']}")


# 示例6: 估值分析
def example_valuation():
    """获取估值分析"""
    from investment_banker import Banker
    
    banker = Banker()
    valuation = banker.valuation("600519")
    
    print(f"股票: {valuation['code']}")
    print(f"当前PE: {valuation['pe']}")
    print(f"历史PE分位: {valuation['pe_percentile']}%")
    print(f"合理价格区间: {valuation['fair_range']}")


# 示例7: 市值管理
def example_market_cap():
    """市值管理建议"""
    from market_cap_manager import Manager
    
    manager = Manager()
    suggestions = manager.optimize("600519")
    
    print(f"股票: {suggestions['code']}")
    print(f"当前市值: {suggestions['market_cap']}")
    print(f"优化建议: {suggestions['suggestions']}")


# 示例8: 综合报告
def example_comprehensive_report():
    """生成综合分析报告"""
    from orchestrator import Orchestrator
    
    orchestrator = Orchestrator()
    report = orchestrator.generate_report(
        codes=["588830", "510300"],
        portfolio_value=500000,
        risk_preference="medium"
    )
    
    print(report)


# ==================== 高级示例 ====================

# 示例9: 自定义Agent组合
def example_custom_team():
    """创建自定义AI团队"""
    from investment_advisor import Advisor
    from industry_researcher import Researcher
    
    # 初始化自定义团队
    team = {
        "advisor": Advisor(),
        "researcher": Researcher(),
    }
    
    # 并行分析
    import concurrent.futures
    
    def analyze(code):
        industry = team["researcher"].analyze(code)
        advice = team["advisor"].diagnose(code)
        return {"industry": industry, "advice": advice}
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(analyze, ["588830", "510300"])
    
    for result in results:
        print(result)


# 示例10: 定时任务
def example_scheduled_task():
    """每日定时分析"""
    import schedule
    import time
    
    from investment_advisor import Advisor
    
    def daily_job():
        advisor = Advisor()
        # 分析关注的股票
        watchlist = ["588830", "510300", "600519"]
        for code in watchlist:
            result = advisor.diagnose(code)
            print(result)
    
    # 每天9:30运行
    schedule.every().day.at("09:30").do(daily_job)
    
    while True:
        schedule.run_pending()
        time.sleep(60)


# ==================== 运行所有示例 ====================

if __name__ == "__main__":
    print("="*60)
    print("Financial Teams 使用示例集锦")
    print("="*60)
    
    # 注意: 以下示例需要配置相应的Agent
    # 实际运行时需要安装akshare等依赖
    
    print("\n示例1: 持仓诊断")
    print("-"*30)
    print("# from investment_advisor import Advisor")
    print("# advisor = Advisor()")
    print("# result = advisor.diagnose('588830', 200000, 4)")
    
    print("\n示例2: ETF推荐")
    print("-"*30)
    print("# from wealth_advisor import WealthAdvisor")
    print("# advisor = WealthAdvisor()")
    print("# etfs = advisor.recommend_etf('medium')")
    
    print("\n示例3: 交易信号")
    print("-"*30)
    print("# from business_opportunity_analyst import Analyst")
    print("# analyst = Analyst()")
    print("# signal = analyst.get_signal('588830')")
    
    print("\n" + "="*60)
    print("更多示例请参考 QUICKSTART.md")
    print("="*60)
