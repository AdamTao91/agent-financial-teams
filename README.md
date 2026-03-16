# Financial Teams - 金融AI Agent团队

> 预配置的专业金融分析Agent团队，支持多角色协作，为投资决策提供全方位支持

[![OpenClaw](https://img.shields.io/badge/OpenClaw-2026.3+-blue)](https://openclaw.ai)
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)]()

## 🎯 简介

**Financial Teams** 是一个免费开源的 OpenClaw 预配置金融Agent库，比 ClawTeam 更专业、更灵活。

- 🤖 **7大金融角色** - 覆盖投研、投行、市值管理、财富管理、交易执行、舆情监控、投资顾问
- 📊 **多角色协作** - 支持团队协同工作，提供综合分析报告
- 📈 **实时行情接入** - 支持A股、ETF、基金等实时数据
- 🔧 **一键安装** - 通过 ClawHub 直接安装

## 📦 安装

```bash
# 安装完整金融团队包
clawdhub install financial-teams

# 或安装单个角色
clawdhub install financial-teams/investment-advisor
```

## 🤖 团队成员

| 角色 | 说明 | 核心功能 |
|------|------|----------|
| **投顾专家** | 综合服务，统筹协调 | 持仓诊断、综合建议 |
| **行业研究员** | 智能投研 | 产业链分析、机会挖掘 |
| **投行专家** | 并购IPO | 资本运作、估值定价 |
| **市值管理助理** | 市值管理 | IR策略、资本运作 |
| **财富专员** | 财富管理 | 资产配置、基金筛选 |
| **商机助理** | 交易信号 | 买卖时机、仓位管理 |
| **企业舆情助理** | 风险监控 | 舆情监测、风险预警 |

## 🔄 协作流程

```
用户持仓查询
    ↓
┌─────────────────────────────────────┐
│  投顾专家（统筹）                   │
│  - 获取实时行情                      │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┬──────────┬──────────┐
    ▼             ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ 行业    │ │ 商机   │ │ 企业   │ │ 财富   │
│ 研究员  │ │ 助理   │ │ 舆情   │ │ 专员   │
└────────┘ └────────┘ └────────┘ └────────┘
    │             │          │          │
    └─────────────┴──────────┴──────────┘
           ↓
┌─────────────────────────────────────┐
│  投顾专家（综合报告）                │
│  - 持仓诊断 - 行业评估              │
│  - 操作建议 - 风险预警              │
│  - 配置建议                        │
└─────────────────────────────────────┘
```

## 📊 功能演示

### 持仓分析示例

```
用户：持有588830，588830元，仓位99.95%

→ 自动获取实时行情
→ 召唤行业研究员分析行业趋势
→ 召唤商机助理分析交易机会
→ 召唤企业舆情助理排查风险
→ 召唤财富专员提供配置建议
→ 投顾专家给出综合诊断报告
```

## 📁 目录结构

```
financial-teams/
├── README.md
├── config.json
├── collaboration-system.md
└── teams/
    ├── investment-advisor/         # 投顾专家
    ├── industry-researcher/       # 行业研究员
    ├── investment-banker/          # 投行专家
    ├── market-cap-manager/         # 市值管理助理
    ├── wealth-advisor/             # 财富专员
    ├── business-opportunity-analyst/ # 商机助理
    └── corporate-sentiment-analyst/ # 企业舆情助理
```

## 🔧 配置

### 配置文件 (config.json)

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

## 🌐 对比

| 特性 | ClawTeam | Financial Teams |
|------|----------|-----------------|
| 金融专业度 | 通用 | ✅ 金融专属 |
| 多角色协作 | 单角色 | ✅ 团队协作 |
| 实时行情 | 需额外配置 | ✅ 内置支持 |
| 中国A股 | 支持有限 | ✅ 全面支持 |
| 开源免费 | 部分收费 | ✅ 完全免费 |

## 📝 使用条款

- 本工具仅供投资参考，不构成投资建议
- 投资有风险，入市需谨慎
- 不承诺任何收益
- 遵守相关法律法规

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License

---

**作者**: Han Li  
**更新**: 2026-03-06
