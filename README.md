# 🎨 AI 圖像生成 Web App

這是一個基於 Python、Streamlit 與官方 `huggingface_hub` 套件建立的 AI 繪圖工具。

## 🚀 功能
- 透過文字提示詞 (Prompt) 生成高品質圖片。
- 支援多款強大開源模型切換，包含：
  - `black-forest-labs/FLUX.1-schnell` (極速、高品質)
  - `stabilityai/sdxl-turbo`
  - `stabilityai/stable-diffusion-xl-base-1.0`
- 支援圖片預覽與下載。
- 安全性設計：使用者需在介面輸入自己的 Hugging Face Token。


## 🛠️ 本地安裝與執行

1. 複製此倉庫：
   ```bash
   git clone https://github.com/jimm1218/ai-texttoimage
   cd 你的倉庫資料夾
   ```
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
