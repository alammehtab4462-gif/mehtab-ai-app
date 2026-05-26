import streamlit as st
import requests
import json

st.set_page_config(page_title="Mehtab Pro AI Workstation", page_icon="🚀", layout="centered")

API_KEY = "AIzaSyAESg2hzplWZS7BtP30TvcEKnKLoKH9udo"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

st.title("🚀 Mehtab Bhai Ka Pro AI Workstation")
st.markdown("---")

st.subheader("🎬 Apna Channel Ya Mood Chunein")
option = st.selectbox(
    "Kis channel ke liye content banana hai?",
    ("The Future India 🇮🇳 (Tech & Future)", "Aam Zindagi 🎬 (Comedy & Shorts)", "Plumbing Business 🛠️ (Professional Ads)", "General Query 🌍 (Normal Sawaal)")
)

if "The Future India" in option:
    channel_name = "The Future India"
    system_instruction = "Tum ek futuristic, high-energy aur patriotic YouTube channel ke content creator ho. Jawab me dhamakedar viral video ideas, scripts aur tags do."
elif "Aam Zindagi" in option:
    channel_name = "Aam Zindagi"
    system_instruction = "Tum ek majedar, comedy aur highly relatable social media creator ho jo aam logon ki zindagi par shorts banata hai. Jawab ekdum desi, funny aur catchy hona chahiye."
elif "Plumbing Business" in option:
    channel_name = "Plumbing Business"
    system_instruction = "Tum ek professional business marketing expert ho. Plumbing services, bathroom installations aur customer attraction ke liye taglines, ideas ya ads likho."
else:
    channel_name = "General Query"
    system_instruction = "Tum ek helpful AI assistant ho. User ke sawaal ka seedha aur badiya jawab Hindi me do."

st.subheader("📁 Media Attachment (Optional)")
uploaded_file = st.file_uploader("Agar kisi photo ya video par script chahiye toh yahan upload karein", type=["jpg", "jpeg", "png", "mp4"])

if uploaded_file is not None:
    st.success(f"✅ {uploaded_file.name} successfully attach ho gayi hai!")

st.subheader(f"📝 [{channel_name}] Ka Topic")
user_topic = st.text_input("Mehtab bhai, aaj kis cheez par video ya ad banana hai? Yahan type karein:")

if st.button("🔥 Generate AI Content"):
    if user_topic:
        hukum = f"Role: {system_instruction}\nTopic: {user_topic}\n\nMujhe ispar badiya content bana kar do Hindi me."
        payload = {"contents": [{"parts": [{"text": hukum}]}]}
        headers = {'Content-Type': 'application/json'}
        st.info("⚡ Gemini Server se connect ho raha hai... Thoda rukiye...")
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                res = response.json()
                jawab = res['candidates'][0]['content']['parts'][0]['text']
                st.success("🎉 Hamara AI Jawab Taiyar Hai!")
                st.markdown(f"### 📢 {channel_name} Special Content:")
                st.write(jawab)
                st.download_button(label="📥 Is Script Ko Save (Download) Karein", data=jawab, file_name=f"{channel_name}_script.txt", mime="text/plain")
            else:
                st.error(f"Server ne error diya: {response.status_code}")
        except Exception as e:
            st.error(f"Kuch dikkat aayi bhai: {e}")
    else:
        st.warning("Mehtab bhai, pehle neeche wale box me kuch topic toh likho!")
