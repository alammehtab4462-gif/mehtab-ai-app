import streamlit as st
import google.generativeai as genai
import os

# Page Configuration (Mobile Friendly Layout)
st.set_page_config(page_title="Mehtab AI Workstation", page_icon="🚀", layout="centered")

# Custom UI Styling
st.markdown("""
    <style>
    .main-title { font-size: 28px; font-weight: bold; color: #FF4B4B; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 Mehtab Bhai Ka Pro AI Workstation</div>', unsafe_allow_html=True)

# API Key Config
API_KEY = ""
if st.secrets and len(st.secrets) > 0:
    API_KEY = list(st.secrets.values())[0]

if not API_KEY:
    API_KEY = os.environ.get("GEMINI_API_KEY", "")

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("🔑 API Key nahi mili! Kripya Streamlit Settings mein apni Key set karein.")

if "form_reset" not in st.session_state:
    st.session_state.form_reset = False

def reset_callback():
    st.session_state.form_reset = True

# App UI Options
channel = st.selectbox("🎬 Apna Channel Ya Mood Chunein", [
    "General Query 🌍 (Normal Sawaal)",
    "The Future India 🇮🇳 (Tech & Future)",
    "Aam Zindagi 🎬 (Comedy & Shorts)",
    "Plumbing Services 🛠️ (Professional Ads)"
])

# File Upload Section
uploaded_file = st.file_uploader("📁 Media Attachment (Optional)", type=["jpg", "png", "mp4"])

if uploaded_file is not None:
    file_type = uploaded_file.type.split('/')[0]
    if file_type == "image":
        st.image(uploaded_file, caption="Uploaded Image Preview", use_container_width=True)
    elif file_type == "video":
        st.video(uploaded_file, format="video/mp4")

# Text input box logic
input_key = "user_prompt_new" if st.session_state.form_reset else "user_prompt_default"
prompt = st.text_input(f"📝 Topic", placeholder="Mehtab bhai, aaj kis cheez par video banana hai?", key=input_key)

col1, col2 = st.columns(2)
with col1:
    generate_click = st.button("🔥 Generate AI Content")
with col2:
    clear_click = st.button("🗑️ Reset / Clear All", on_click=reset_callback)

if st.session_state.form_reset:
    st.session_state.form_reset = False
    st.rerun()

# Processing AI Request
if generate_click:
    if not prompt and not uploaded_file:
        st.warning("⚠️ Kripya koi prompt likhein ya file upload karein!")
    elif not API_KEY:
        st.error("⚠️ AI Connect nahi ho sakta kyunki API Key missing hai.")
    else:
        with st.spinner("⚡ Gemini Server se connect ho raha hai..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                content_parts = []
                if uploaded_file:
                    bytes_data = uploaded_file.read()
                    content_parts.append({"mime_type": uploaded_file.type, "data": bytes_data})
                if prompt:
                    content_parts.append(prompt)
                
                response = model.generate_content(content_parts)
                st.balloons()
                st.success("🎉 Hamara Al Jawab Taiyar Hai!")
                st.markdown("### 📢 Special Content:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error aaya bhai: {str(e)}")
