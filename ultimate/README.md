# Financial Teams ULTIMATE 🥇

<p align="center">
  <img src="https://img.shields.io/badge/Financial-Teams_ULTIMATE-blue" alt="Ultimate">
  <img src="https://img.shields.io/badge/OpenBB-Integrated-green" alt="OpenBB">
  <img src="https://img.shields.io/badge/vnpy-Integrated-green" alt="vnpy">
  <img src="https://img.shields.io/badge/akshare-Native-green" alt="akshare">
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
</p>

> 🥇 **全球首个整合三大顶级金融平台的AI投资系统**

---

## 🏆 整合架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Financial Teams ULTIMATE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │    OpenBB    │  │    vnpy      │  │   akshare    │             │
│  │  (全球数据)   │  │  (交易框架)   │  │  (A股数据)   │             │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘             │
│         │                  │                  │                    │
│         └──────────────────┼──────────────────┘                    │
│                            ▼                                        │
│                   ┌──────────────┐                                 │
│                   │   DataHub    │  ← 统一数据中枢                   │
│                   └──────┬───────┘                                 │
│                          ▼                                          │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    7+3 AI Agent 协作                         │   │
│  │  投顾│行业│技术│财报│量化│缠论│舆情│策略│风控│              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                            ▼                                        │
│                   ┌──────────────┐                                 │
│                   │ 用户报告输出  │  ← 9维度诊断                    │
│                   └──────────────┘                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 已整合功能

### 1. 数据源 (DataHub)

| 数据源 | 功能 | 状态 |
|--------|------|------|
| **akshare** | A股/期货/基金/宏观 | ✅ 内置 |
| **OpenBB** | 全球市场/加密货币 | ✅ 可选 |
| **yfinance** | 美股/港股 | ✅ 可选 |
| **tushare** | A股/新三板 | 🔄 规划 |

### 2. 交易框架 (TradingEngine)

| 功能 | 来源 | 状态 |
|------|------|------|
| **回测引擎** | vnpy概念 | ✅ 自研 |
| **实盘接口** | vnpy概念 | 🔄 规划 |
| **订单管理** | vnpy概念 | ✅ |
| **持仓管理** | vnpy概念 | ✅ |
| **风控模块** | vnpy概念 | ✅ |

### 3. 技术分析 (TechAnalysis)

| 指标库 | 功能 | 状态 |
|--------|------|------|
| **TA-Lib** | 100+技术指标 | ✅ 可选 |
| **numpy** | 基础计算 | ✅ 内置 |
| **pandas** | 数据处理 | ✅ 内置 |
| **自研缠论** | 分型/笔/中枢 | ✅ 独有 |

---

## 🚀 快速开始

### 安装

```bash
# 基础版 (推荐)
pip install akshare pandas numpy

# 完整版 (含OpenBB + TA-Lib)
pip install akshare pandas numpy openbb talib

# 克隆项目
git clone https://github.com/AdamTao91/agent-financial-teams
```

### 使用

```python
from ultimate import FinancialTeamsUltimate

# 初始化
ft = FinancialTeamsUltimate()

# A股分析
result = ft.analyze('588830', market='china')

# 完整诊断
report = ft.full_diagnostic('588830', cost=1.0, position=200000)

# 运行策略
ft.run_strategy('momentum', ['588830', '000001'])
```

### CLI

```bash
# 分析股票
python cli.py analyze 588830

# 生成报告
python cli.py report 588830 1.00 200000

# 运行策略
python cli.py quant momentum
```

---

## 📊 功能对比

| 功能 | Financial Teams | OpenBB | vnpy | akshare |
|------|----------------|--------|------|---------|
| **AI Agent协作** | ✅ 独有 | ❌ | ❌ | ❌ |
| **9维度诊断** | ✅ 独有 | ❌ | ❌ | ❌ |
| **缠论分析** | ✅ 独有 | ❌ | ❌ | ❌ |
| **中文A股** | ✅ | ❌ | ✅ | ✅ |
| **全球市场** | ✅ | ✅ | ❌ | ❌ |
| **回测框架** | ✅ | ✅ | ✅ | ❌ |
| **实盘交易** | 🔄 | ❌ | ✅ | ❌ |
| **免费开源** | ✅ | ✅ | ✅ | ✅ |

---

## 🎯 独特优势

1. **Agent协作** - 7+3专业Agent团队
2. **中文优化** - 专注A股/ETF/基金
3. **缠论分析** - 自动笔/中枢/背驰
4. **免费开源** - 无付费门槛
5. **一站式** - 数据+分析+策略+风控

---

## 📁 项目结构

```
financial-teams/
├── ultimate/                 # ULTIMATE整合版
│   └── __init__.py          # 统一入口
├── technical-analyst/       # 技术分析
├── chan-analyst/            # 缠论分析
├── quant-factor/            # 量化因子
├── financial-report-analyst/ # 财报分析
├── comprehensive_report.py  # 诊断报告
├── cli.py                   # CLI工具
└── README.md
```

---

## ⚡ 下一步

- [ ] 添加tushare数据支持
- [ ] 实盘交易接口
- [ ] Docker一键部署
- [ ] Web界面
- [ ] 移动APP

---

**口号: 让每个人都有一个AI投资顾问团队**

```bash
pip install akshare && git clone https://github.com/AdamTao91/agent-financial-teams
```
