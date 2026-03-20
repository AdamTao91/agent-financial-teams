# Financial Teams - 快速开始指南

## 5秒快速开始

```python
# 方式1: 安装使用
pip install akshare yfinance
git clone https://github.com/AdamTao91/agent-financial-teams.git

# 方式2: 直接运行
cd agent-financial-teams
python3 demo.py 588830 200000 4
```

## 完整示例

### 1. 持仓诊断

```python
from investment_advisor import Advisor

advisor = Advisor()
result = advisor.diagnose("588830", position=200000, holding_months=4)
print(result)
```

### 2. 行业分析

```python
from industry_researcher import Researcher

researcher = Researcher()
report = researcher.analyze("新能源", depth="deep")
print(report)
```

### 3. ETF推荐

```python
from wealth_advisor import WealthAdvisor

advisor = WealthAdvisor()
recommendations = advisor.recommend_etf(risk_level="medium")
for etf in recommendations:
    print(f"{etf['code']}: {etf['name']}")
```

### 4. 交易信号

```python
from business_opportunity_analyst import Analyst

analyst = Analyst()
signal = analyst.get_signal("588830")
print(f"信号: {signal['action']}, 置信度: {signal['confidence']}%")
```

## API 速查表

| 模块 | 功能 | 关键方法 |
|------|------|---------|
| investment-advisor | 投顾综合服务 | diagnose() |
| industry-researcher | 行业研究 | analyze() |
| investment-banker | 投行服务 | valuation() |
| market-cap-manager | 市值管理 | optimize() |
| wealth-advisor | 财富管理 | recommend_etf() |
| business-opportunity | 交易信号 | get_signal() |
| corporate-sentiment | 舆情监控 | monitor() |

## 常见问题

**Q: 支持哪些市场?**
A: A股、ETF、基金、港股、美股

**Q: 数据从哪里来?**
A: akshare (免费开源库)

**Q: 需要API Key吗?**
A: 不需要，akshare和yfinance都是免费的

## 获取帮助

- 📝 提交 Issue: https://github.com/AdamTao91/agent-financial-teams/issues
- ⭐ Star 支持: https://github.com/AdamTao91/agent-financial-teams

---
*让每个散户都拥有AI投资顾问* 🧠💰
