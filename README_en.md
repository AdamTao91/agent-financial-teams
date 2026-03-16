# Financial Teams - Professional Financial AI Agent

<p align="center">
  <a href="https://openclaw.ai"><img src="https://img.shields.io/badge/Powered%20by-OpenClaw-blue" alt="OpenClaw"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/stargazers"><img src="https://img.shields.io/github/stars/AdamTao91/agent-financial-teams" alt="Stars"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/blob/main/LICENSE"><img src="https://img.shields.io/github/license/AdamTao91/agent-financial-teams" alt="License"></a>
  <a href="https://github.com/AdamTao91/agent-financial-teams/releases"><img src="https://img.shields.io/github/v/release/AdamTao91/agent-financial-teams" alt="Version"></a>
</p>

> Pre-configured professional financial AI agent team with multi-role collaboration, providing comprehensive support for investment decisions.

## 🎯 Introduction

**Financial Teams** is a free and open-source OpenClaw pre-configured financial AI agent library. More professional and flexible than ClawTeam.

### Key Features

- 🤖 **7 Specialized Financial Roles** - Covering investment research, investment banking, market cap management, wealth management, trade execution, sentiment monitoring, and investment advisory
- 📊 **Multi-Role Collaboration** - Team synergy for comprehensive analysis reports
- 📈 **Real-Time Market Data** - Support for A-shares, ETFs, funds, and more
- 🔧 **One-Click Installation** - Install directly via ClawHub

## 📦 Installation

```bash
# Install complete financial team package
clawdhub install financial-teams

# Or install individual roles
clawdhub install financial-teams/investment-advisor
clawdhub install financial-teams/industry-researcher
clawdhub install financial-teams/investment-banker
```

## 🤖 Team Members

| Role | Description | Core Functions |
|------|-------------|----------------|
| Investment Advisor | Comprehensive service, coordination | Portfolio diagnosis, integrated recommendations |
| Industry Researcher | Investment research | Industry chain analysis, opportunity discovery |
| Investment Banker | M&A & IPO | Capital operations, valuation |
| Market Cap Manager | Market cap management | IR strategy, capital operations |
| Wealth Advisor | Wealth management | Asset allocation, fund selection |
| Business Analyst | Trading signals | Entry/exit timing, position management |
| Sentiment Analyst | Risk monitoring | Sentiment monitoring, risk alerts |

## 🔄 Collaboration Workflow

```
User Portfolio Query
        ↓
┌─────────────────────────────────────┐
│    Investment Advisor (Coordinator) │
│    - Fetch Real-Time Quotes         │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┬──────────┬──────────┐
    ▼             ▼          ▼          ▼
┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
│Industry│  │Business│  │Sentiment│  │Wealth  │
│Research│  │Analyst │  │Analyst  │  │Advisor │
└────────┘  └────────┘  └────────┘  └────────┘
    │             │          │          │
    └─────────────┴──────────┴──────────┘
                  ↓
┌─────────────────────────────────────┐
│    Investment Advisor (Report)      │
│    - Portfolio Diagnosis           │
│    - Industry Evaluation           │
│    - Action Recommendations        │
│    - Risk Alerts                   │
│    - Allocation Suggestions        │
└─────────────────────────────────────┘
```

## 📊 Demo

**Portfolio Analysis Example:**

```
User: Holding 588830 (ETF), 588,830 CNY, 99.95% position
↓
Auto-fetch real-time quotes
↓
Summon Industry Researcher for trend analysis
↓
Summon Business Analyst for trading opportunities
↓
Summon Sentiment Analyst for risk checking
↓
Summon Wealth Advisor for allocation suggestions
↓
Investment Advisor delivers comprehensive report
```

## 📁 Directory Structure

```
financial-teams/
├── README.md
├── config.json
├── collaboration-system.md
└── teams/
    ├── investment-advisor/      # Investment Advisor
    ├── industry-researcher/     # Industry Researcher
    ├── investment-banker/       # Investment Banker
    ├── market-cap-manager/      # Market Cap Manager
    ├── wealth-advisor/         # Wealth Advisor
    ├── business-opportunity-analyst/  # Business Analyst
    └── corporate-sentiment-analyst/   # Sentiment Analyst
```

## 🔧 Configuration

### config.json

```json
{
  "name": "Financial Teams",
  "version": "1.0.0",
  "model": "minimax-portal/MiniMax-M2.5",
  "capabilities": {
    "voice": true,
    "memory": true,
    "collaboration": true
  }
}
```

## 🌐 Comparison

| Feature | ClawTeam | Financial Teams |
|---------|----------|-----------------|
| Financial Expertise | General | ✅ Financial-specific |
| Multi-Role Collaboration | Single role | ✅ Team collaboration |
| Real-Time Quotes | Requires setup | ✅ Built-in support |
| China A-Share | Limited support | ✅ Full support |
| Open Source | Partial free | ✅ Completely free |

## 📝 Disclaimer

- This tool is for investment reference only, not investment advice
- Investment involves risks, proceed with caution
- No returns are guaranteed
- Comply with relevant laws and regulations

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

## 📄 License

MIT License

---

**Author:** Han Li  
**Last Updated:** 2026-03-13
