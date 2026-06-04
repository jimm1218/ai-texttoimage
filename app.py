import streamlit as st
import io
from PIL import Image
import os
from huggingface_hub import InferenceClient

# 設定頁面資訊
st.set_page_config(page_title="AI 圖像生成器", page_icon="🎨")

st.title("🎨 AI 圖像生成 Web App")
st.write("輸入一段文字，讓 AI 為你創作圖片。")

def generate_image(prompt, token, model_id):
    """使用官方 huggingface_hub 庫發送請求"""
    if not token:
        st.error("❌ 請先在左側邊欄輸入你的 Hugging Face Access Token。")
        return None

    try:
        client = InferenceClient(model=model_id, token=token)
        # text_to_image 會自動處理重試與 503 等待，並直接回傳 PIL.Image 格式
        image = client.text_to_image(prompt)
        return image
    except Exception as e:
        error_msg = str(e)
        st.error(f"❌ 圖片生成失敗！")
        with st.expander("🛠️ 點此查看詳細錯誤資訊 (Debug)"):
            st.code(error_msg)
        return None

# 側邊欄設定
with st.sidebar:
    st.header("🔑 安全設定")
    user_token = st.text_input("輸入 Hugging Face Token:", type="password", help="請從你的 Hugging Face Settings > Tokens 取得 (需有 Read 權限)")
    st.info("提示：此 Token 僅用於此次請求，不會被儲存。")
    
    st.divider()
    st.header("⚙️ 模型設定")
    model_id = st.selectbox(
        "選擇 AI 模型:",
        (
            "black-forest-labs/FLUX.1-schnell",
            "stabilityai/sdxl-turbo", 
            "stabilityai/stable-diffusion-xl-base-1.0",
            "nvidia/Cosmos3-Super-Text2Image"
        ),
        help="推薦使用 FLUX.1-schnell 或 sdxl-turbo，出圖速度最快且品質穩定。"
    )

# 介面佈局
with st.form("gen_form"):
    prompt = st.text_area("請輸入提示詞 (Prompt):", placeholder="An astronaut riding a horse on mars, hd, dramatic lighting")
    submit = st.form_submit_button("開始生成")

if submit:
    if not prompt:
        st.warning("請輸入提示詞！")
    else:
        with st.spinner("AI 正在繪圖中，請稍候..."):
            image = generate_image(prompt, user_token, model_id)
            
            if image:
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
