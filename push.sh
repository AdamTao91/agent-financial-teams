#!/bin/bash
# Financial Teams - 一键推送脚本

# 使用方法:
# 1. 设置GitHub Token: export GH_TOKEN="你的token"
# 2. 运行: bash push.sh

# 或者直接运行并输入token:
# echo "请输入GitHub Token: "
# read TOKEN
# GH_TOKEN=$TOKEN bash push.sh

if [ -z "$GH_TOKEN" ]; then
    echo "❌ 请设置GH_TOKEN环境变量"
    echo "   方法1: export GH_TOKEN='你的GitHubtoken'"
    echo "   方法2: 在GitHub设置 -> Developer settings -> Personal access tokens -> Generate new token"
    exit 1
fi

echo "🔄 正在推送代码到GitHub..."

# 使用token推送
git remote set-url origin https://${GH_TOKEN}@github.com/AdamTao91/agent-financial-teams.git
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ 推送成功!"
else
    echo "❌ 推送失败，请检查token权限"
fi
