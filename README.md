# Financial Teams

<div align="center">

![Logo](https://img.shields.io/badge/Financial%20Teams-7%20AI%20Agents-blue)
![Stars](https://img.shields.io/github/stars/AdamTao91/agent-financial-teams)
![License](https://img.shields.io/github/license/AdamTao91/agent-financial-teams)
![Python](https://img.shields.io/badge/Python-3.10+-green)

让每个散户都拥有专业的AI投资团队

[English](./README_en.md) | [中文](./README_CN.md)

</div>

## ⭐ 简介

**Financial Teams** 是一个免费开源的 OpenClaw 预配置金融AI Agent库，7大AI角色协作，为投资决策提供全方位支持。

## 🚀 特性

- 🤖 **7大金融AI角色** - 投研、投行、市值管理、财富管理、交易执行、舆情监控、投资顾问
- 📊 **多角色协作** - 团队协同工作，提供综合分析报告
- 📈 **实时行情** - 支持A股、ETF、基金实时数据
- 🔧 **一键安装** - 通过ClawHub直接安装
- 💰 **完全免费** - 开源免费，无付费功能

## 📦 安装

```bash
# 方式1: ClawHub安装
clawdhub install financial-teams

# 方式2: 克隆使用
git clone https://github.com/AdamTao91/agent-financial-teams.git
cd agent-financial-teams
pip install -r requirements.txt
```

## 💻 快速开始

```python
# 运行演示
python3 demo.py 588830 200000 4
```

输出示例:
```
🚀 FINANCIAL TEAMS - AI金融分析报告
📌 分析对象: 鹏华科创新能源ETF (588830)
🤖 7大AI Agent 协作分析中...
📋 分析报告
  • 综合评分: 72/100
  • 建议操作: 持有观察
```

## 📁 目录结构

```
agent-financial-teams/
├── demo.py                 # 演示脚本
├── examples.py             # 使用示例
├── cli.py                  # 命令行工具
├── orchestrator.py         # 协调器
├── config.json             # 配置文件
├── SKILL.md                # Skill定义
├── README.md               # 中文文档
├── README_en.md            # 英文文档
├── QUICKSTART.md           # 快速开始
├── API.md                  # API文档
├── COMPARISON.md           # 竞品对比
├── CONTRIBUTING.md         # 贡献指南
├── CHANGELOG.md            # 更新日志
└── teams/                  # 7大AI角色
    ├── investment-advisor/
    ├── industry-researcher/
    ├── investment-banker/
    ├── market-cap-manager/
    ├── wealth-advisor/
    ├── business-opportunity-analyst/
    └── corporate-sentiment-analyst/
```

## 🤖 7大AI角色

| 角色 | 功能 |
|------|------|
| 投顾专家 | 持仓诊断、综合建议 |
| 行业研究员 | 产业链分析、机会挖掘 |
| 投行专家 | 资本运作、估值定价 |
| 市值管理助理 | IR策略、资本运作 |
| 财富专员 | 资产配置、基金筛选 |
| 商机助理 | 买卖时机、仓位管理 |
| 企业舆情助理 | 舆情监测、风险预警 |

## 📊 竞品对比

| 特性 | Financial Teams | OpenBB | Qlib |
|------|-----------------|--------|------|
| AI Agent | ✅ 7个 | ❌ | ❌ |
| 中国A股 | ✅ 完整 | ✅ | ✅ |
| 免费 | ✅ 完全免费 | ✅ | ✅ |
| 安装复杂度 | ⭐ 简单 | 中等 | 中等 |

## 🔗 链接

- ⭐ Star: https://github.com/AdamTao91/agent-financial-teams
- 📖 文档: https://github.com/AdamTao91/agent-financial-teams#readme
- 🐛 Issues: https://github.com/AdamTao91/agent-financial-teams/issues

## 📄 License

MIT License

---

**投资有风险，入市需谨慎** ⚠️
