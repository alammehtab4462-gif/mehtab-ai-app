
import streamlit as st
import google.generativeai as genai
import os

# Page Configuration
st.set_page_config(page_title="Mehtab AI Workstation", page_icon="🚀", layout="centered")

# Custom UI Styling for Chat
st.markdown("""
    <style>
    .main-title { font-size: 28px; font-weight: bold; color: #FF4B4B; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .chat-bubble-user { background-color: #E2F0CB; padding: 12px; border-radius: 12px; margin-bottom: 10px; color: black; text-align: right; }
    .chat-bubble-ai { background-color: #F0F2F6; padding: 12px; border-radius: 12px; margin-bottom: 10px; color: black; text-align: left; }
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

# Initialize Chat History in Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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

# Text input box for continuous chatting
prompt = st.text_input("📝 Apna Sawaal Likhein", placeholder="Mehtab bhai, yahan apna sawaal likhein ya aage ki baat poochein...")

col1, col2 = st.columns(2)
with col1:
    generate_click = st.button("🔥 Send / Ask AI")
with col2:
    clear_click = st.button("🗑️ Reset Chat / Clear All")

if clear_click:
    st.session_state.chat_history = []
    st.rerun()

# Processing Request
if generate_click:
    if not prompt and not uploaded_file:
        st.warning("⚠️ Kripya kuch likhein ya file upload karein!")
    elif not API_KEY:
        st.error("⚠️ AI Connect nahi ho sakta kyunki API Key missing hai.")
    else:
        with st.spinner("⚡ Gemini Jawab taiyar kar raha hai..."):
            try:
                # Using latest gemini-2.5-flash model
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                # Strict instructions to respond in Hindi/Hinglish
                system_prompt = (
                    "Aap Mehtab Alam ke personal AI assistant hain. Aapko sakti se hamesha saral, "
                    "dilchasp aur asardar HINDI (ya Hinglish) mein hi jawab dena hai. Kisi bhi haal mein "
                    "English mein bada jawab na likhein, balki Roman Script/Hinglish ya Hindi font ka use karein. "
                )
                
                if "The Future India" in channel:
                    system_prompt += "Aapka focus deshbhakti, tech, aur crazy viral facts par hona chahiye jo YouTube Reels par chha sakein."
                elif "Aam Zindagi" in channel:
                    system_prompt += "Aapka focus relatable comedy, mazaakiya kisse aur funny short script par hona chahiye."
                elif "Plumbing Services" in channel:
                    system_prompt += "Aapka focus professional plumbing ads, slogans aur service promotion par hona chahiye."

                # Building full context with chat history so it remembers previous discussion
                full_prompt = f"{system_prompt}\n\n"
                for role, text in st.session_state.chat_history:
                    full_prompt += f"{role}: {text}\n"
                
                full_prompt += f"User: {prompt}"
                
                content_parts = []
                if uploaded_file:
                    bytes_data = uploaded_file.read()
                    content_parts.append({"mime_type": uploaded_file.type, "data": bytes_data})
                
                content_parts.append(full_prompt)
                
                response = model.generate_content(content_parts)
                
                # Save current message and response to history
                st.session_state.chat_history.append(("User", prompt if prompt else "[Uploaded File]"))
                st.session_state.chat_history.append(("AI", response.text))
                
            except Exception as e:
                st.error(f"❌ Error aaya bhai: {str(e)}")

# Displaying Chat History in proper UI blocks
if st.session_state.chat_history:
    st.markdown("### 💬 Aapki Baatchit (Chat History):")
    # Displaying latest message on top or in normal sequence
    for role, text in st.session_state.chat_history:
        if role == "User":
            st.markdown(f'<div class="chat-bubble-user"><b>Aap:</b> {text}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-ai"><b>AI Assistant:</b><br>{text}</div>', unsafe_allow_html=True)
