#!/usr/bin/env python3
"""
Financial Teams Demo - 金融AI Agent团队演示

一个命令即可获得专业的投资分析报告
7大AI角色协作，全面分析股票/ETF

用法:
    python demo.py                    # 默认分析示例
    python demo.py 588830             # 分析指定ETF
    python demo.py 588830 200000      # 分析并带入持仓
    python demo.py --cli               # 交互式CLI模式
"""

import sys
import json
from datetime import datetime

# ==================== 模拟的AI分析结果 ====================

def get_stock_info(code):
    """获取股票基本信息"""
    stock_db = {
        "588830": {"name": "鹏华科创新能源ETF", "type": "ETF", "price": 1.688, "change": -1.23},
        "510300": {"name": "沪深300ETF", "type": "ETF", "price": 3.892, "change": 0.45},
        "600519": {"name": "贵州茅台", "type": "Stock", "price": 1685.00, "change": -2.15},
        "000858": {"name": "五粮液", "type": "Stock", "price": 128.50, "change": 1.08},
    }
    return stock_db.get(code, {"name": f"股票{code}", "type": "Stock", "price": 10.00, "change": 0.0})


def analyze_with_agents(code, position=0, holding_months=0):
    """模拟7大AI Agent协作分析"""
    stock = get_stock_info(code)
    
    print("\n" + "="*70)
    print("🚀 FINANCIAL TEAMS - AI金融分析报告")
    print("="*70)
    print(f"📅 分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📌 分析对象: {stock['name']} ({code})")
    print(f"📊 资产类型: {stock['type']}")
    
    if position > 0:
        print(f"💰 持仓金额: {position:,.0f}元")
        if holding_months > 0:
            print(f"📆 持仓时间: {holding_months}个月")
    
    print("\n" + "-"*70)
    print("🤖 7大AI Agent 协作分析中...")
    print("-"*70)
    
    # 模拟Agent协作
    agents = [
        ("📈 投顾专家", "综合分析中...", "✅ 完成"),
        ("🔍 行业研究员", "分析行业趋势...", "✅ 完成"),
        ("💼 投行专家", "评估估值水平...", "✅ 完成"),
        ("📊 市值管理", "分析市场情绪...", "✅ 完成"),
        ("💰 财富专员", "提供配置建议...", "✅ 完成"),
        ("🎯 商机助理", "计算买卖时机...", "✅ 完成"),
        ("🛡️ 企业舆情", "监控风险因素...", "✅ 完成"),
    ]
    
    for i, (agent, status, done) in enumerate(agents):
        print(f"  {agent}: {status} {done}")
        if i < 2:
            import time
            time.sleep(0.3)
    
    print("\n" + "="*70)
    print("📋 分析报告")
    print("="*70)
    
    # 核心分析结果
    print(f"""
【{stock['name']} ({code})】

📈 行情状态:
  • 当前价格: {stock['price']:.3f}
  • 今日涨跌幅: {stock['change']:+.2f}%
  • 趋势判断: {'📈 上涨趋势' if stock['change'] > 0 else '📉 下跌趋势'}

🎯 投资建议:
  • 综合评分: 78/100 (中等偏上)
  • 建议操作: {'建议持有' if stock['change'] > -2 else '建议关注'}
  • 仓位建议: 30-50% 

⚠️ 风险提示:
  • 市场有风险，投资需谨慎
  • 本报告仅供参考，不构成投资建议
  • 过去业绩不代表未来表现
""")
    
    if position > 0:
        profit = (stock['price'] * 0.15 - 1.0) * position  # 模拟收益
        print(f"""
💵 持仓诊断:
  • 当前估值: {position:,.0f}元
  • 模拟盈亏: {profit:+,.0f}元 ({profit/position*100:+.1f}%)
  • 建议: {'继续持有，观察一周' if profit > 0 else '可考虑补仓'}
""")
    
    print("="*70)
    print("✨ 分析完成 - 感谢使用 Financial Teams!")
    print("="*70)
    
    return True


def cli_mode():
    """交互式CLI模式"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║           🤖 FINANCIAL TEAMS - 交互式分析工具               ║
╠══════════════════════════════════════════════════════════════╣
║  输入股票/ETF代码进行分析                                     ║
║  示例: 588830, 510300, 600519                                ║
║  输入 'quit' 退出                                            ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    while True:
        try:
            code = input("\n📊 请输入股票/ETF代码: ").strip()
            if code.lower() in ['quit', 'q', 'exit']:
                print("👋 再见!")
                break
            
            if not code:
                continue
                
            position = input("💰 持仓金额(元，直接回车跳过): ").strip()
            position = int(position) if position else 0
            
            holding = input("📆 持仓月数(直接回车跳过): ").strip()
            holding = int(holding) if holding else 0
            
            analyze_with_agents(code, position, holding)
            
        except KeyboardInterrupt:
            print("\n👋 再见!")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")


def main():
    """主函数"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║         🚀 FINANCIAL TEAMS - 金融AI Agent 团队               ║
║         📊 7大AI角色协作 | 全方位投资分析                    ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    args = sys.argv[1:]
    
    if '--cli' in args or '-i' in args:
        cli_mode()
    elif len(args) >= 1:
        code = args[0]
        position = int(args[1]) if len(args) > 1 else 0
        holding_months = int(args[2]) if len(args) > 2 else 0
        analyze_with_agents(code, position, holding_months)
    else:
        # 默认演示
        print("📌 默认分析示例: 588830 (鹏华科创新能源ETF)")
        print("📌 用法: python demo.py <代码> <持仓金额> <持仓月数>\n")
        analyze_with_agents("588830", 200000, 4)


if __name__ == "__main__":
    main()
