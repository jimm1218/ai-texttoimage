# ️ 專案生成提示詞紀錄 (Development Prompts)

這份文件紀錄了我們用來生成與優化此 AI 圖像生成 Web App 的核心溝通提示詞（Prompts）。
如果你未來想從零開始讓 AI 幫你寫出類似的專案，可以參考以下循序漸進的對話歷程：

## 🚀 階段一：建立核心架構 (MVP)
**初始開發 Prompt：**
> 「完成一個可部署的 AI 圖像生成 Web App。且需要使用 Hugging Face 上的免費模型因為我用 cosmos3 無法生成出圖，建立一個可以輸入文字 prompt 並產生圖片的應用程式。」

## 🛡️ 階段二：提升安全性與靈活性
**安全性優化 Prompt：**
> 「他不能讓我在介面輸入我的 TOKEN 嗎？我不想把 TOKEN 放在程式內。」

## 🔧 階段三：解決網路與模型穩定性問題 (Debug)
在 Streamlit Cloud 部署後，遇到免費伺服器 DNS 解析失敗的常見問題。
**除錯 Prompt：**
> 「我在 streamlist 執行還是一直出現這個錯誤：ConnectionError: HTTPSConnectionPool... DNS 解析失敗」
*💡 AI 解決方案：捨棄手動 `requests`，改用官方 `huggingface_hub` 套件，完美解決自動重試與網路阻擋問題。*

## ⚙️ 階段四：擴充多模型支援
**擴充功能 Prompt：**
> 「你幫我看一下我有改 API 了 (更換模型)」
> 「再幫我新增一個模型 black-forest-labs/FLUX.1-schnell」

## 🔑 階段五：本地開發環境的最佳實踐 (突破性重點)
在本地端測試時，成功抓出缺乏環境變數套件的問題，確立了最安全且便利的開發模式。
**關鍵突破 Prompt：**
> 「我把 requirements 多了 python-dotenv 就成功了」
*💡 開發者洞察：確立了使用 `python-dotenv` 讀取隱藏的 `.env` 檔案，既能保護機密 Token 不外洩，又解決了本地開發需反覆手動輸入的痛點。*

---

### 💡 總結心得
開發這類 AI 應用的關鍵在於：
1. **高度重視資訊安全 (重點)**：絕對不要把密碼寫死在代碼裡。結合 UI 輸入與 `python-dotenv` 讀取 `.env` 檔案，是兼顧安全與便利的業界標準實踐。
2. **善用官方 SDK**（如 `huggingface_hub`），可以幫你省下大量處理網路錯誤與重試的心力！
