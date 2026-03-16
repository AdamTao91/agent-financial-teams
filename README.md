# Financial Teams - 🥇 全球首个整合型AI投资平台

<p align="center">
  <a href="https://github.com/AdamTao91/agent-financial-teams/stargazers"><img src="https://img.shields.io/github/stars/AdamTao91/agent-financial-teams" alt="Stars"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/blob/main/LICENSE"><img src="https://img.shields.io/github/license/AdamTao91/agent-financial-teams" alt="License"></a>
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
  <img src="https://img.shields.io/badge/akshare-Native-green" alt="akshare">
  <img src="https://img.shields.io/badge/yfinance-Integrated-green" alt="yfinance">
</p>

> 🤖 **全球首个整合akshare + yfinance + vnpy概念的AI Agent团队** | 7+3专业Agent | 9维度诊断 | 免费开源

---

## 🏆 已整合功能

### 数据源
| 数据源 | 功能 | 状态 |
|--------|------|------|
| **akshare** | A股/期货/基金/宏观 | ✅ 内置 |
| **yfinance** | 美股/港股 | ✅ 已安装 |
| **OpenBB** | 全球市场 | ⚠️ 可选 |

### 交易框架 (vnpy概念)
- ✅ 回测引擎
- ✅ 订单管理
- ✅ 持仓管理
- ✅ 风控模块

### 技术指标
- ✅ MA/EMA均线
- ✅ MACD
- ✅ RSI
- ✅ 布林带
- ✅ KDJ
- ⚠️ TA-Lib (可选)

### 缠论分析
- ✅ 分型识别
- ✅ 笔的分析
- ✅ 背驰判断

---

## 🚀 安装

```bash
# 基础版
pip install akshare pandas numpy yfinance

# 完整版
pip install akshare pandas numpy yfinance openbb

# 克隆
git clone https://github.com/AdamTao91/agent-financial-teams
```

---

## 💡 使用

```python
from ultimate import FinancialTeamsUltimate

ft = FinancialTeamsUltimate()

# A股分析
result = ft.analyze('588830', market='china')

# 美股分析
apple = ft.datahub.get_us_stock('AAPL')
print(f"AAPL: ${apple['price']}")

# 技术分析
macd = ft.tech.macd(prices)
rsi = ft.tech.rsi(prices)
```

---

## 📁 项目结构

```
financial-teams/
├── ultimate/                  # ULTIMATE整合版 🥇
│   └── __init__.py           # 统一入口
├── technical-analyst/        # 技术分析
├── chan-analyst/            # 缠论分析
├── quant-factor/            # 量化因子
├── comprehensive_report.py  # 9维度诊断
└── cli.py                   # CLI工具
```

---

## ⭐ 安装命令

```bash
pip install akshare pandas numpy yfinance
git clone https://github.com/AdamTao91/agent-financial-teams
cd agent-financial-teams
python ultimate/__init__.py
```
