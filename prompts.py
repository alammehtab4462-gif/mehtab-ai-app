import streamlit as st

# Page configuration for a professional tech look
st.set_page_config(page_title="Cute Let Prompt - Premium AI Hub", page_icon="✨", layout="centered")

# Premium Custom CSS for Professional Dark-Gold Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
    }
    .main-title {
        font-size: 32px;
        font-weight: 800;
        color: #F59E0B;
        text-align: center;
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .sub-title {
        font-size: 13px;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 500;
    }
    .card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #334155;
        border-left: 6px solid #F59E0B;
        margin-bottom: 20px;
    }
    .tag-trending {
        background-color: #059669;
        color: #A7F3D0;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Website Header Section
st.markdown('<div class="main-title">✨ CUTE LET PROMPT ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">100% Original Face Identity | Top Viral Instagram Reels Trends</div>', unsafe_allow_html=True)

# Purely Trending & Video-Specific 4 Prompts Data
prompts_data = [
    {
        "title": "1. Instagram Multi-Layer Aesthetic Triple Exposure (Playvo Trend)", 
        "type": "🔥 New Trend",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000078736.jpg",
        "prompt": "Create a trending multi-exposure edit from this reference image. Keep the exact original face identity, features, and expressions 100% unchanged. Background shows a large faded close-up profile of the person with sunglasses. Foreground shows a sharp full-body version of the same person standing confidently in a pastel pink shirt and white trousers. Clean, artistic background texture, high contrast, cinematic."
    },
    {
        "title": "2. Royal Golden Birthday Special Poster Trend (First AI Visual Tool Style)", 
        "type": "🔥 New Trend",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000078737.jpg",
        "prompt": "Convert this image into a birthday poster edit. 100% preserve the original face, eyes, and smile without changes. Combine a faded close-up background with a sharp full-body foreground layout. The background should be a rich abstract brown-gold watercolor wash texture with subtle particle effects. Include elegant golden cursive text at the top reading 'HAPPY Birthday stylish pic'."
    },
    {
        "title": "3. Instagram Viral Name Art Crown Edit (Aanya Style)", 
        "type": "Viral Overlay",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000079493.jpg",
        "prompt": "Create a trending double-exposure style edit from this image. Retain the exact original face structure and identity without any modifications. Blend a large faded profile portrait in the background with a clear foreground shot. The background is a moody aesthetic forest with orange butterflies. Add clean gold typography text above reading 'Aanya' with a small royal crown icon."
    },
    {
        "title": "4. Patriotic Bhagat Singh Style Abstract Art", 
        "type": "Trending Art",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000079586.jpg",
        "prompt": "Patriotic portrait style. The subject's face shape and core features must remain completely recognizable and realistic. Modify only the outfit and styling to include a classic vintage fedora hat and mustache like Bhagat Singh. Background is a striking scarlet red abstract dynamic watercolor texture. Emotional cinematic lighting."
    }
]

# Display Loop
for item in prompts_data:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<span class="tag-trending">{item["type"]}</span>', unsafe_allow_html=True)
    st.markdown(f"### {item['title']}")
        
    try:
        st.image(item['image_url'], use_container_width=True)
    except:
        st.info("💡 Image preview is syncing from GitHub...")
        
    st.markdown("**📋 Copy Prompt:**")
    st.code(item['prompt'], language="text")
    st.markdown('</div>', unsafe_allow_html=True)
