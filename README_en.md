# Financial Teams - 英文版README

# Financial Teams - Next-Gen AI Investment Research Platform

<p align="center">
  <a href="https://openclaw.ai"><img src="https://img.shields.io/badge/Powered%20by-OpenClaw-blue" alt="OpenClaw"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/stargazers"><img src="https://img.shields.io/github/stars/AdamTao91/agent-financial-teams" alt="Stars"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/blob/main/LICENSE"><img src="https://img.shields.io/github/license/AdamTao91/agent-financial-teams" alt="License"></a>
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Chinese%20A-Stocks-Data-green" alt="A-Stocks">
</p>

> 🤖 World's Most Powerful Open-Source Financial AI Agent Team | 7+3 Agents Collaboration | Comprehensive Investment Research | Free & Open Source

[中文](./README.md) | [Demo](#-demo) | [Quick Start](#-installation) | [Documentation](#-documentation)

---

## 🎯 Why Financial Teams?

| Feature | Traditional Tools | Financial Teams |
|---------|-------------------|----------------|
| **AI Agents** | Single AI Response | 7+3 Agent Team |
| **Analysis Depth** | Simple Q&A | 9 Dimensions |
| **Real-time Data** | Needs Setup | ✅ Built-in A-shares/ETF |
| **Technical Analysis** | Basic Indicators | MA/K-line/Chan/Factors |
| **Financial Reports** | None | Auto Analysis |
| **Installation** | Complex | ```pip install``` |
| **Price** | Paid SaaS | ✅ Free & Open |

---

## 🏆 Core Features

### 1. Multi-Agent Collaboration System
```
User: "Analyze ETF 588830"

→ Investment Advisor receives request
   ↓
   ├── Industry Researcher - Sector trends
   ├── Technical Analyst - K-line/MA/MACD/Chan Theory
   ├── Financial Report - Valuation/PE/ROE
   ├── Quant Factor - Multi-factor stock selection
   ├── Sentiment Analyst - News & sentiment
   └── Wealth Advisor - Asset allocation
   
   ↓
→ Investment Advisor compiles final report
   ↓
→ User receives comprehensive investment report
```

### 2. Comprehensive Diagnostic Report (9 Dimensions)

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | Basic Info | Code/Type/Realtime quote |
| 2 | Position Diagnosis | Cost/Position/Returns |
| 3 | Technical Analysis | CoT reasoning |
| 4 | Industry Analysis | Holdings/Themes |
| 5 | Chan Theory |笔/中枢/背驰/买卖点 |
| 6 | Quant Factors | Momentum/Value/Growth/Quality |
| 7 | Risk Radar | Position/Industry/Valuation |
| 8 | Conclusion | Score/Target/Stop-loss |
| 9 | Action Plan | Conservative/Aggressive/Flexible |

### 3. Built-in Real-time Data
- ✅ A-share realtime quotes (akshare)
- ✅ ETF/LOF funds
- ✅ Sector rotation
- ✅ Money flow monitoring
- ✅ Financial news sentiment

### 4. Professional Technical Analysis
- 📊 Moving Averages (MA5/10/20/60/120/250)
- 📈 MACD/KDJ/RSI/CCI/BOLL
- 🕯️ 100+ Candlestick Patterns
- 🧮 Chan Theory Analysis (分型/笔/中枢/背驰)
- 📉 Quantitative Factor Library

### 5. Financial Report Analysis
- 📋 Annual/Quarterly Report Auto-parse
- 💰 PE/PB/ROE/ROA Metrics
- 📊 Peer Comparison
- 🎯 Valuation Assessment

---

## 📦 Installation

### Method 1: pip (Recommended)
```bash
pip install akshare pandas numpy

# Clone project
git clone https://github.com/AdamTao91/agent-financial-teams

# Run example
cd agent-financial-teams
python comprehensive_report.py
```

### Method 2: OpenClaw/ClawHub
```bash
clawdhub install financial-teams
```

---

## 💡 Quick Start

### 1. Generate Diagnostic Report
```python
from comprehensive_report import generate_report

# Basic analysis
report = generate_report("588830")

# Full analysis (with position)
report = generate_report(
    code="588830",
    cost=1.00,
    position=200000,
    position_pct=99
)

print(report)
```

### 2. Technical Analysis
```python
from technical_analyst import TechnicalAnalyzer

analyzer = TechnicalAnalyzer()
result = analyzer.full_analysis("588830")

print(result['overall'])  # Strong bullish / Neutral / Strong bearish
print(result['ma_signals'])  # MA signals
print(result['macd'])  # MACD indicators
```

### 3. Chan Theory Analysis
```python
from chan_analyzer import ChanAnalyzer

chan = ChanAnalyzer()
result = chan.full_analysis("000001")

print(result['signals'])  # Buy/sell signals
print(result['trend'])  # Trend judgment
```

### 4. Quantitative Stock Selection
```python
from quant_factor import QuantFactorEngine

engine = QuantFactorEngine()
result = engine.smart_select("growth")

print(result['stocks'])  # Growth stocks list
```

---

## 📊 Demo Output

```
======================================================================
🐮 Financial Teams v2.0 - ETF Diagnostic Report
======================================================================
【Dimension 1: Basic Info】
  Fund Code: 588830
  Fund Name: 鹏华科创板新能源ETF
  Latest NAV: 1.688
  Daily Change: -1.23%

【Dimension 2: Position Diagnosis】
  Investment: $30,000 USD
  📈 Estimated Return: +68.8% ≈ +$13,800

【Dimension 3: Technical Analysis】
  MA System: Consolidation pattern
  MACD: Waiting for direction
  Technical Score: 54/100

...

======================================================================
📊 Overall Score: 61/100 ⚠️ Neutral
💡 Strategy: Hold with caution
```

---

## 📁 Project Structure

```
financial-teams/
├── comprehensive_report.py    # Full diagnostic report generator
├── technical_analyst/        # Technical analysis agent
│   ├── SKILL.md
│   └── technical_analyzer.py
├── financial_report_analyst/ # Financial report agent
├── quant_factor/             # Quant factor agent
├── chan_analyst/            # Chan theory agent
├── investment-advisor/       # Investment advisor
├── industry-researcher/       # Industry researcher
└── README.md
```

---

## 🔧 Tech Stack

- **AI Framework**: OpenClaw
- **LLMs**: MiniMax / Claude / GPT / DeepSeek
- **Data**: akshare, baostock, tushare
- **Analysis**: pandas, numpy
- **Python**: 3.8+

---

## 📈 Comparison with Competitors

| Project | Stars | Focus | Our Advantage |
|---------|-------|-------|----------------|
| **vnpy** | 37k+ | Quant Framework | ✅ AI Agents + Chinese |
| **FinRobot** | 6k+ | Multi-LLM | ✅ A-shares focus + Local |
| **阿布量化** | 16k+ | Chan Theory | ✅ Agent Collaboration + Free |
| **zipline** | 19k+ | Backtest | ✅ Real-time Analysis + Chinese |

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing`)
5. Submit Pull Request

---

## 📝 License

MIT License - See [LICENSE](./LICENSE)

---

## ⚠️ Disclaimer

- This tool is for educational purposes only
- Not financial advice
- Invest at your own risk
- Past performance does not guarantee future results

---

## ⭐ Star Us

If you find this project helpful, please give us a ⭐!

```bash
git clone https://github.com/AdamTao91/agent-financial-teams
```

---

**🌐 Website**: https://financial-teams.dev  
**📧 Email**: hello@financial-teams.dev  
**💬 Discord**: https://discord.gg/financial-teams

---

<p align="center">Built with ❤️ on OpenClaw | © 2026 Financial Teams</p>
