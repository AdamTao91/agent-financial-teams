# Financial Teams API 参考

## 目录

1. [投资顾问 (Investment Advisor)](#投资顾问-investment-advisor)
2. [行业研究员 (Industry Researcher)](#行业研究员-industry-researcher)
3. [投行专家 (Investment Banker)](#投行专家-investment-banker)
4. [市值管理 (Market Cap Manager)](#市值管理-market-cap-manager)
5. [财富专员 (Wealth Advisor)](#财富专员-wealth-advisor)
6. [商机助理 (Business Opportunity Analyst)](#商机助理-business-opportunity-analyst)
7. [企业舆情 (Corporate Sentiment Analyst)](#企业舆情-corporate-sentiment-analyst)

---

## 投资顾问 (Investment Advisor)

负责统筹协调，综合分析

### Advisor.diagnose()

持仓诊断主方法

```python
from investment_advisor import Advisor

advisor = Advisor()
result = advisor.diagnose(
    code="588830",           # 股票/基金代码
    position=200000,         # 持仓金额(元)
    holding_months=4,        # 持仓月数
    risk_preference="medium" # 风险偏好: low/medium/high
)
```

**参数:**
| 参数 | 类型 | 说明 |
|------|------|------|
| code | str | 股票或基金代码 |
| position | float | 持仓金额(元) |
| holding_months | int | 持仓月数 |
| risk_preference | str | 风险偏好 |

**返回:**
```python
{
    "code": "588830",
    "name": "鹏华科创板新能源ETF",
    "price": 1.688,
    "change": -1.23,
    "recommendation": "持有",
    "score": 72,
    "target_price": 1.75,
    "stop_loss": 1.55,
    "analysis": {...}
}
```

---

## 行业研究员 (Industry Researcher)

负责行业分析和机会挖掘

### Researcher.analyze()

```python
from industry_researcher import Researcher

researcher = Researcher()
result = researcher.analyze(
    industry="新能源车",    # 行业名称
    depth="deep"          # 分析深度: quick/deep
)
```

---

## 投行专家 (Investment Banker)

负责估值和资本运作

### Banker.valuation()

```python
from investment_banker import Banker

banker = Banker()
valuation = banker.valuation(
    code="600519",
    method="dcf"  # 估值方法: pe/dcf/peg
)
```

---

## 市值管理 (Market Cap Manager)

负责市值管理和IR策略

### Manager.optimize()

```python
from market_cap_manager import Manager

manager = Manager()
suggestions = manager.optimize(
    code="600519",
    target_market_cap=100000000000  # 目标市值(元)
)
```

---

## 财富专员 (Wealth Advisor)

负责资产配置和基金筛选

### WealthAdvisor.recommend_etf()

```python
from wealth_advisor import WealthAdvisor

advisor = WealthAdvisor()
etfs = advisor.recommend_etf(
    risk_level="medium",  # low/medium/high
    amount=100000,        # 投资金额
    duration=12           # 投资期限(月)
)
```

### WealthAdvisor.asset_allocation()

```python
allocation = advisor.asset_allocation(
    total=1000000,        # 总资产
    age=30,              # 年龄
    risk_score=70        # 风险评分 0-100
)
```

---

## 商机助理 (Business Opportunity Analyst)

负责交易信号和时机把握

### Analyst.get_signal()

```python
from business_opportunity_analyst import Analyst

analyst = Analyst()
signal = analyst.get_signal(
    code="588830",
    period="short"  # short/medium/long
)
```

**返回:**
```python
{
    "code": "588830",
    "action": "买入",  # 买入/卖出/持有
    "confidence": 75,
    "entry_price": 1.68,
    "target_price": 1.80,
    "stop_loss": 1.55,
    "reason": "技术指标显示超卖..."
}
```

---

## 企业舆情 (Corporate Sentiment Analyst)

负责风险监控和舆情分析

### Analyst.monitor()

```python
from corporate_sentiment_analyst import Analyst

analyst = Analyst()
risks = analyst.monitor(
    codes=["588830", "600519"],
    alert_level="medium"  # low/medium/high
)
```

### Analyst.news()

```python
news = analyst.news(
    code="600519",
    days=7  # 最近N天
)
```

---

## 错误处理

所有API都支持异常处理:

```python
try:
    advisor = Advisor()
    result = advisor.diagnose("588830", 200000, 4)
except ValueError as e:
    print(f"参数错误: {e}")
except ConnectionError as e:
    print(f"网络错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
```

---

*更多API请参考源代码*
