# Financial Teams

<div align="center">

### 🤖 7大AI角色协作 | 📊 全方位投资分析

[⭐ Star](https://github.com/AdamTao91/agent-financial-teams/stargazers)
[📖 文档](https://github.com/AdamTao91/agent-financial-teams#readme)
[🐛 Issues](https://github.com/AdamTao91/agent-financial-teams/issues)

让每个散户都拥有专业的AI投资团队

</div>

---

## ✨ 特性

| 特性 | 说明 |
|------|------|
| 🤖 7大AI角色 | 投顾/行业/投行/市值/财富/商机/舆情 |
| 📊 多Agent协作 | 团队智能，综合分析 |
| 📈 实时行情 | A股/ETF/基金/港股/美股 |
| 🔧 多种使用方式 | CLI/API/Bot/Colab/Docker |
| 💰 完全免费 | 开源免费，无付费功能 |

## 🚀 快速开始

```bash
# 安装
pip install akshare yfinance
git clone https://github.com/AdamTao91/agent-financial-teams.git

# 运行
cd agent-financial-teams
python demo.py 588830 200000 4
```

## 📦 多种运行方式

| 方式 | 命令 |
|------|------|
| 🖥️ 演示脚本 | `python demo.py 588830` |
| 🌐 Web API | `python api.py` |
| 🤖 Telegram Bot | `python bot.py` |
| 🐳 Docker | `docker build -t ft . && docker run -p 8000:8000 ft` |
| ☁️ Colab | 打开 colab.ipynb |

## 📁 项目结构

```
agent-financial-teams/
├── demo.py              # 演示脚本
├── api.py               # Web API
├── bot.py               # Telegram Bot
├── cli.py               # 命令行工具
├── orchestrator.py      # AI协调器
├── Dockerfile           # Docker配置
├── colab.ipynb          # Colab笔记本
├── requirements.txt    # 依赖
├── SKILL.md             # Skill定义
└── teams/               # 7大AI角色
    ├── investment-advisor/
    ├── industry-researcher/
    └── ...
```

## 🤖 7大AI角色

1. **投顾专家** - 综合服务，统筹协调
2. **行业研究员** - 产业链分析，机会挖掘
3. **投行专家** - 资本运作，估值定价
4. **市值管理** - IR策略，资本运作
5. **财富专员** - 资产配置，基金筛选
6. **商机助理** - 买卖时机，仓位管理
7. **企业舆情** - 舆情监测，风险预警

## 📊 对比

| | Financial Teams | OpenBB | Qlib |
|--|-----------------|--------|------|
| AI Agent | ✅ 7个 | ❌ | ❌ |
| 免费 | ✅ 完全 | ✅ | ✅ |
| 中国A股 | ✅ 完整 | ✅ | ✅ |
| 安装 | ⭐ 简单 | 中等 | 中等 |

## 🔗 链接

- ⭐ https://github.com/AdamTao91/agent-financial-teams
- 📖 https://github.com/AdamTao91/agent-financial-teams#readme

## ⚠️ 声明

投资有风险，入市需谨慎

---

⭐ Star支持我们!
