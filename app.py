import streamlit as st
import requests
import io
from PIL import Image
import os
import time

# 設定頁面資訊
st.set_page_config(page_title="AI 圖像生成器", page_icon="🎨")

st.title("🎨 AI 圖像生成 Web App")
st.write("輸入一段文字，讓 AI 為你創作圖片。")

# 設定 Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/nvidia/Cosmos3-Super-Text2Image"

def query(payload, token):
    """發送請求至 Hugging Face Inference API"""
    if not token:
        st.error("❌ 請先在左側邊欄輸入你的 Hugging Face Access Token。")
        return None

    headers = {"Authorization": f"Bearer {token}"}

    max_retries = 3
    for attempt in range(max_retries):
        try:
            # 增加 timeout 參數 (例如 60 秒)，避免伺服器回應過慢導致連線強行中斷
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                return response.content
            elif response.status_code == 503:
                if attempt < max_retries - 1:
                    time.sleep(5)  # 模型冷啟動，等待 5 秒後自動重試
                    continue
                st.warning("⚠️ 模型正在 Hugging Face 伺服器上載入中（冷啟動），請稍候 20-30 秒後再次點擊生成。")
                return None
            elif response.status_code == 401:
                st.error("❌ Token 無效，請檢查你的 Hugging Face Token 是否正確且具備 Read 權限。")
                return None
            else:
                st.error(f"API 請求失敗 (Status: {response.status_code}): {response.text}")
                return None
                
        except requests.exceptions.ConnectionError as e:
            if attempt < max_retries - 1:
                time.sleep(3)  # 網路抖動，等待 3 秒後自動重試連線
                continue
            st.error("📡 網路連線錯誤：無法連接到 Hugging Face 伺服器。這通常是 Streamlit Cloud 的暫時性網路問題。")
            with st.expander("🛠️ 點此查看詳細錯誤資訊 (Debug)"):
                st.code(str(e))
            return None
        except Exception as e:
            st.error(f"❌ 發生非預期錯誤: {e}")
            with st.expander("🛠️ 點此查看詳細錯誤資訊 (Debug)"):
                st.code(str(e))
            return None
            
    return None

# 側邊欄設定
with st.sidebar:
    st.header("🔑 安全設定")
    user_token = st.text_input("輸入 Hugging Face Token:", type="password", help="請從你的 Hugging Face Settings > Tokens 取得 (需有 Read 權限)")
    st.info("提示：此 Token 僅用於此次請求，不會被儲存。")

# 介面佈局
with st.form("gen_form"):
    prompt = st.text_area("請輸入提示詞 (Prompt):", placeholder="An astronaut riding a horse on mars, hd, dramatic lighting")
    submit = st.form_submit_button("開始生成")

if submit:
    if not prompt:
        st.warning("請輸入提示詞！")
    else:
        with st.spinner("AI 正在繪圖中，請稍候..."):
            image_bytes = query({"inputs": prompt}, user_token)
            
            if image_bytes:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=f"生成結果: {prompt}", use_column_width=True)
                
                # 下載按鈕
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="下載圖片",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png"
                )

st.info("註：若生成失敗，可能是 Hugging Face 免費伺服器正在載入模型，請稍等一分鐘後再試。")
