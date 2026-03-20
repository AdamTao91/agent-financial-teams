# Financial Teams Docker 配置

## 快速开始

```bash
# 构建镜像
docker build -t financial-teams:latest .

# 运行
docker run -p 8000:8000 financial-teams:latest
```

## 使用说明

1. 确保已安装 Docker
2. 构建镜像: `docker build -t financial-teams .`
3. 运行: `docker run -p 8000:8000 financial-teams`
4. 访问: http://localhost:8000

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| PORT | 服务端口 | 8000 |
| LOG_LEVEL | 日志级别 | info |
| DATA_CACHE | 缓存时间(秒) | 300 |

## API端点

- `GET /health` - 健康检查
- `GET /api/v1/analyze?code=xxx` - 分析股票
- `GET /api/v1/portfolio?positions=xxx` - 持仓诊断
