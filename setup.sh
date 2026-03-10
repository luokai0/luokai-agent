#!/bin/bash
echo "🐉 Setting up Luo Kai Agent..."
pip install groq openai requests python-dotenv ddgs pandas openpyxl playwright
sudo rm -f /etc/apt/sources.list.d/yarn.list
sudo apt-get update -qq
sudo apt-get install -y libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2t64
python -m playwright install chromium
echo "✅ Luo Kai Agent ready! Run: python agent.py"
