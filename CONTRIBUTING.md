# 贡献指南

感谢您对 Financial Teams 的兴趣!

## 如何贡献

### 1. 报告 Bug

请通过 [GitHub Issues](https://github.com/AdamTao91/agent-financial-teams/issues) 报告:

```markdown
## Bug描述
[描述问题]

## 复现步骤
1. ...
2. ...

## 期望行为
[描述期望]

## 实际行为
[描述实际]
```

### 2. 提出新功能

```markdown
## 功能建议
[描述功能]

## 使用场景
[描述使用场景]

## 期望实现
[代码示例如果有]
```

### 3. 提交代码

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 4. 完善文档

- 修正拼写错误
- 添加使用示例
- 翻译文档

## 开发环境设置

```bash
# 克隆项目
git clone https://github.com/AdamTao91/agent-financial-teams.git
cd agent-financial-teams

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 运行测试
python -m pytest
```

## 代码规范

- 使用 Python 3.10+
- 遵循 PEP 8
- 添加 docstrings
- 添加类型注解

## 行为准则

- 保持友好和包容
- 尊重不同意见
- 专注于社区利益

---

有问题? 欢迎提交 Issue 或 PR!
