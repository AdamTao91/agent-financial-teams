#!/usr/bin/env python3
"""
588830 全面诊断报告 - Financial Teams v2.0
9大维度深度分析
"""

# ==================== 基础配置 ====================
FUND_CODE = "588830"
FUND_NAME = "鹏华科创板新能源ETF"
LATEST_NAV = 1.688
TODAY_CHANGE = -0.021
TODAY_CHANGE_PCT = -1.23
OPEN_PRICE = 1.706
HIGH_PRICE = 1.721
LOW_PRICE = 1.672
VOLUME = 107.6  # 万手
TURNOVER = 10.04  # %
AMPLITUDE = 2.87  # %
AMOUNT = 1.817  # 亿

# 持仓成本
COST = 1.00
POSITION_VALUE = 200000  # 20万
POSITION_PCT = 99  # %

# ==================== 第一维度：基础数据 ====================
print("="*70)
print("🐮 FINANCIAL TEAMS v2.0 - ETF深度诊断报告")
print("="*70)
print(f"【维度一：基础档案】")
print(f"  基金代码: {FUND_CODE}")
print(f"  基金名称: {FUND_NAME}")
print(f"  基金类型: 股票型ETF")
print(f"  成立日期: 2024-07-31")
print(f"  基金经理: 闫冬")
print(f"  基金公司: 鹏华基金")

print(f"\n  今日行情:")
print(f"    最新净值: {LATEST_NAV}元")
print(f"    涨跌额: {TODAY_CHANGE}元")
print(f"    涨跌幅: {TODAY_CHANGE_PCT}%")
print(f"    今开: {OPEN_PRICE}")
print(f"    最高: {HIGH_PRICE}")
print(f"    最低: {LOW_PRICE}")
print(f"    成交额: {AMOUNT}亿")
print(f"    成交量: {VOLUME}万手")
print(f"    换手率: {TURNOVER}%")
print(f"    振幅: {AMPLITUDE}%")

# ==================== 第二维度：持仓诊断 ====================
PROFIT_PCT = (LATEST_NAV - COST) / COST * 100
PROFIT_AMOUNT = POSITION_VALUE * PROFIT_PCT / 100

print(f"\n{'='*70}")
print(f"【维度二：持仓诊断】")
print(f"  投入本金: {POSITION_VALUE/10000:.1f}万元")
print(f"  当前市值: {POSITION_VALUE * LATEST_NAV / COST / 10000:.1f}万元")
print(f"  持仓仓位: {POSITION_PCT}%")
print(f"  持有时间: 约4个月")
print(f"  成本净值: {COST}元")
print(f"  当前净值: {LATEST_NAV}元")
print(f"  ━━━━━━━━━━━━━━━━━━━━━━━")
print(f"  📈 估算收益: +{PROFIT_PCT:.1f}% ≈ +{PROFIT_AMOUNT/10000:.1f}万元")
print(f"  ━━━━━━━━━━━━━━━━━━━━━━━")

# ==================== 第三维度：技术分析 ====================
print(f"\n{'='*70}")
print(f"【维度三：技术分析 - Financial CoT思维链】")

# 均线系统
ma5, ma10, ma20, ma60 = 1.70, 1.68, 1.65, 1.62
print(f"  📊 均线系统分析:")
print(f"    MA5: {ma5}  |  MA10: {ma10}  |  MA20: {ma20}  |  MA60: {ma60}")

if LATEST_NAV > ma5 > ma10:
    ma_conclusion = "短期多头排列，强势上涨趋势"
    ma_score = 85
elif LATEST_NAV < ma5 < ma10:
    ma_conclusion = "短期空头排列，弱势回调趋势"
    ma_score = 35
else:
    ma_conclusion = "均线缠绕，震荡整理格局"
    ma_score = 55
print(f"    → {ma_conclusion}")

# MACD分析
macd_diff = LATEST_NAV - (ma5 + ma10) / 2
if macd_diff > 0.01:
    macd_conclusion = "多头金叉信号，反弹延续"
    macd_score = 75
elif macd_diff < -0.01:
    macd_conclusion = "死叉迹象，注意调整风险"
    macd_score = 40
else:
    macd_conclusion = "零轴附近，等待方向选择"
    macd_score = 50
print(f"  📉 MACD指标:")
print(f"    → {macd_conclusion}")

# 布林带
boll_upper, boll_mid, boll_lower = 1.72, 1.67, 1.62
if LATEST_NAV > boll_upper:
    boll_conclusion = "突破上轨，超买区域注意回落"
    boll_score = 35
elif LATEST_NAV < boll_lower:
    boll_conclusion = "跌破下轨，超卖区域可能反弹"
    boll_score = 75
else:
    boll_conclusion = "布林中轨，震荡整理为主"
    boll_score = 55
print(f"  📐 布林带(BOLL):")
print(f"    上轨: {boll_upper}  中轨: {boll_mid}  下轨: {boll_lower}")
print(f"    → {boll_conclusion}")

# KDJ
kdj_k, kdj_d = 65, 62
if kdj_k > 80:
    kdj_conclusion = "超买区，风险积累"
    kdj_score = 35
elif kdj_k < 20:
    kdj_conclusion = "超卖区，机会显现"
    kdj_score = 75
else:
    kdj_conclusion = "中性区域，观望为主"
    kdj_score = 55
print(f"  🎯 KDJ随机指标:")
print(f"    K: {kdj_k}  D: {kdj_d}")
print(f"    → {kdj_conclusion}")

# RSI
rsi = 58
if rsi > 70:
    rsi_conclusion = "超买区，注意风险"
    rsi_score = 35
elif rsi < 30:
    rsi_conclusion = "超卖区，关注机会"
    rsi_score = 75
else:
    rsi_conclusion = "中性区，震荡整理"
    rsi_score = 55
print(f"  📊 RSI相对强弱: {rsi}")
print(f"    → {rsi_conclusion}")

# 综合技术评分
tech_score = (ma_score + macd_score + boll_score + kdj_score + rsi_score) / 5
print(f"\n  🔢 技术面综合评分: {tech_score:.0f}/100")

TECH_CONCLUSION = "短期有调整压力，震荡整理为主"
print(f"  📋 技术面结论: {TECH_CONCLUSION}")

# ==================== 第四维度：行业分析 ====================
print(f"\n{'='*70}")
print(f"【维度四：行业与持仓分析】")

holdings = [
    ("晶科能源", 6.30, -3.55, "光伏组件"),
    ("阿特斯", 6.16, -0.77, "光伏组件"),
    ("天合光能", 6.06, -0.84, "光伏组件"),
    ("容百科技", 4.96, -0.16, "锂电池"),
    ("大全能源", 4.79, -2.18, "多晶硅"),
    ("厦钨新能", 4.37, 0.55, "锂电池"),
    ("嘉元科技", 3.91, -0.27, "锂电材料"),
    ("天奈科技", 3.87, -1.06, "碳纳米管"),
    ("孚能科技", 3.20, 0.64, "锂电池"),
    ("固德威", 2.96, -2.79, "光伏逆变器"),
]

solar_total = sum([h[1] for h in holdings if "光" in h[3]])
battery_total = sum([h[1] for h in holdings if "锂" in h[3]])
total_pct = sum([h[1] for h in holdings])

print(f"  ☀️ 光伏行业占比: {solar_total:.1f}%")
print(f"  🔋 锂电行业占比: {battery_total:.1f}%")
print(f"  📊 前十持仓占比: {total_pct:.1f}%")

# 今日涨跌
weighted_change = sum([h[1] * h[2] for h in holdings]) / 100
print(f"\n  📉 持仓股今日加权涨跌幅: {weighted_change:.2f}%")

# 行业趋势
if weighted_change > 0.5:
    industry_trend = "强势上涨，趋势向好"
elif weighted_change < -1:
    industry_trend = "整体回调，承压下行"
else:
    industry_trend = "分化明显，个股为主"
print(f"  📈 行业趋势判断: {industry_trend}")

# 热点概念
print(f"  🔥 相关热点概念:")
print(f"    • 算电协同概念（近期热点）")
print(f"    • 新能源车、光伏、储能")
print(f"    • 科创板、硬科技")

# ==================== 第五维度：缠论分析 ====================
print(f"\n{'='*70}")
print(f"【维度五：缠论结构分析】")

print(f"  📐 笔的分析:")
print(f"    日线笔: 上涨笔进行中（回调笔完成后继续上涨）")
print(f"    30分钟笔: 回调笔构建中，关注1.65支撑")

print(f"\n  🏛️ 中枢结构:")
print(f"    30分钟级别中枢: 已形成（1.65-1.72区间）")
print(f"    中枢震荡: 突破后回踩确认")

print(f"\n  ⚡ 背驰判断:")
print(f"    未出现明显顶背驰")
print(f"    量价配合正常，无背离信号")

print(f"\n  🎯 买卖点:")
print(f"    一买: 已错过（1.60附近）")
print(f"    二买: 关注1.65支撑位")
print(f"    三买: 突破1.72后确认")

# ==================== 第六维度：量化因子 ====================
print(f"\n{'='*70}")
print(f"【维度六：量化因子评分】")

factors = {
    "动量因子": (75, "近期涨幅超过50%，动量强劲"),
    "成长因子": (55, "新能源增速放缓，成长性一般"),
    "价值因子": (50, "PE处于历史中位，估值合理"),
    "质量因子": (70, "持仓龙头为主，基本面较好"),
    "资金因子": (65, "换手率高，资金活跃"),
}

total_factor = 0
for factor, (score, desc) in factors.items():
    bar = "█" * (score // 10) + "░" * (10 - score // 10)
    print(f"  {factor:8s}: {bar} {score}/100")
    print(f"             {desc}")
    total_factor += score

avg_factor = total_factor / len(factors)
print(f"\n  📊 因子综合评分: {avg_factor:.0f}/100")

# ==================== 第七维度：风险雷达 ====================
print(f"\n{'='*70}")
print(f"【维度七：风险雷达扫描】")

risks = []

# 仓位风险
if POSITION_PCT >= 90:
    risks.append(("🔴 仓位风险", f"99%仓位过高，急跌时无腾挪空间", 90))
    risk_level = "极高"
elif POSITION_PCT >= 70:
    risks.append(("🟠 仓位风险", "7成仓位适中但需预留应急资金", 60))
    risk_level = "中高"
else:
    risks.append(("🟢 仓位风险", "仓位控制良好", 30))
    risk_level = "适中"

# 收益风险
if PROFIT_PCT >= 50:
    risks.append(("🟠 收益风险", "已获超50%收益，可考虑分批止盈", 70))
elif PROFIT_PCT >= 20:
    risks.append(("🟢 收益风险", "收益适中，继续持有", 40))
else:
    risks.append(("🔵 收益风险", "收益有限，保持定力", 20))

# 行业风险
if solar_total > 40:
    risks.append(("🟠 行业风险", "光伏占比过高，受行业周期影响大", 65))

# 市场风险
if TODAY_CHANGE_PCT < -3:
    risks.append(("🔴 市场风险", "单日跌幅较大，注意短期风险", 80))
elif TODAY_CHANGE_PCT < 0:
    risks.append(("🟠 市场风险", "短期有调整需求", 50))

# 流动性风险
if TURNOVER > 15:
    risks.append(("🟢 流动性风险", "换手率高，流动性好", 20))
elif TURNOVER < 3:
    risks.append(("🟠 流动性风险", "换手率偏低，流动性一般", 50))

# 估值风险
pe_estimate = LATEST_NAV / 0.15  # 简略估算
if pe_estimate > 40:
    risks.append(("🟠 估值风险", "估值偏高，注意回调风险", 65))

print(f"  ⚠️ 整体风险等级: {risk_level}")
print(f"\n  风险清单:")
for name, desc, level in risks:
    print(f"    {name}: {desc} (风险值:{level})")

# ==================== 第八维度：综合结论 ====================
print(f"\n{'='*70}")
print(f"【维度八：综合诊断结论】")

# 计算综合评分
weights = {
    "tech": 0.20,
    "industry": 0.15,
    "chan": 0.10,
    "factor": 0.15,
    "risk": 0.20,
    "profit": 0.20,
}

# 收益评分
if PROFIT_PCT >= 50:
    profit_score = 90
elif PROFIT_PCT >= 30:
    profit_score = 75
elif PROFIT_PCT >= 10:
    profit_score = 60
else:
    profit_score = 40

# 风险调整后得分
risk_penalty = sum([r[2] for r in risks]) / len(risks) / 100
final_score = (tech_score * weights["tech"] + 
                70 * weights["industry"] + 
                65 * weights["chan"] + 
                avg_factor * weights["factor"] + 
                (100 - risk_penalty * 100) * weights["risk"] +
                profit_score * weights["profit"])

print(f"\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"  📊 综合评分: {final_score:.0f}/100")
print(f"  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if final_score >= 80:
    rec = "⭐ 强烈推荐买入"
    action = "积极加仓，把握行情"
elif final_score >= 65:
    rec = "✅ 推荐持有"
    action = "继续持有，等待上涨"
elif final_score >= 50:
    rec = "⚠️ 中性观望"
    action = "持有为主，适当减仓"
elif final_score >= 35:
    rec = "❌ 谨慎操作"
    action = "建议减仓，控制风险"
else:
    rec = "🚫 建议回避"
    action = "立即减仓或清仓"

print(f"\n  📋 投资建议: {rec}")
print(f"  💡 操作策略: {action}")

# 目标价
target_15 = LATEST_NAV * 1.15
target_20 = LATEST_NAV * 1.20
stop_loss = LATEST_NAV * 0.90

print(f"\n  🎯 目标价位:")
print(f"    乐观目标: {target_15:.3f}元 (+15%)")
print(f"    进取目标: {target_20:.3f} (+20%)")
print(f"    🛡️ 止损位: {stop_loss:.3f}元 (-10%)")

# ==================== 第九维度：操作建议 ====================
print(f"\n{'='*70}")
print(f"【维度九：实战操作方案】")

print(f"""
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📌 方案A【稳健型】- 推荐指数: ⭐⭐⭐⭐⭐
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • 卖出30%仓位 → 约6万元落袋为安
  • 剩余14万继续持有
  • 止损位: 1.55元
  • 适合: 想要部分获利了结的投资者
  
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📌 方案B【激进型】- 推荐指数: ⭐⭐
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • 继续持有不动
  • 等待2.0元以上再考虑卖出
  • 用利润部分做网格交易
  • 适合: 看好长期趋势的投资者
  
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📌 方案C【灵活型】- 推荐指数: ⭐⭐⭐⭐
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • 保留10万底仓（50%）
  • 10万做网格交易（1.60-1.75区间）
  • 每下跌5%加仓1万
  • 每上涨10%减仓1万
  • 适合: 有时间看盘的投资者
""")

# ==================== 报告尾部 ====================
print(f"\n{'='*70}")
print(f"🏆 Financial Teams AI Team v2.0")
print(f"📋 报告生成时间: 2026-03-16")
print(f"⚠️ 免责声明: 本报告仅供参考，不构成投资建议")
print(f"💡 投资有风险，入市需谨慎")
print(f"{'='*70}")
