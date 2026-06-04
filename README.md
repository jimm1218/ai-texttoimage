# 🎨 AI 圖像生成 Web App

這是一個使用 Python、Streamlit 與 Hugging Face Inference API 建立的簡單 AI 繪圖工具。

## 🚀 功能
- 透過文字提示詞 (Prompt) 生成高品質圖片。
- 整合 Hugging Face 免費模型 `Stable Diffusion XL`。
- 支援圖片預覽與下載。
- 安全性設計：使用者需在介面輸入自己的 Hugging Face Token。

## 🛠️ 本地安裝與執行

1. 複製此倉庫：
   ```bash
   git clone <你的-github-倉庫網址>
   ```
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 執行應用程式：
   ```bash
   streamlit run app.py
   ```