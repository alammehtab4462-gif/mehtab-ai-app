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
    .tag-boy {
        background-color: #1E3A8A;
        color: #93C5FD;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .tag-girl {
        background-color: #701A75;
        color: #F472B6;
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
st.markdown('<div class="sub-title">Premium 4K AI Prompts | Viral Instagram & Reels Photo Editing Trends</div>', unsafe_allow_html=True)

# 12 Instagram Viral Trends Prompts Data
prompts_data = [
    # --- TOP REELS VIRAL TRENDS (FROM VIDEO) ---
    {
        "title": "1. Instagram Multi-Layer Aesthetic Triple Exposure", "type": "Trending",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000078736.jpg",
        "prompt": "Create a viral Instagram trending triple-exposure portrait from this photo. The subject's exact original face, facial features, expressions, and natural skin tone must remain 100% identical and unchanged. The background features a large, artistic, semi-transparent profile portrait of the face with sharp sunglasses. In the center, blend a medium shot looking directly at the camera. In the foreground, show the full-body figure standing confidently, dressed in a stylish pastel pink button-up shirt and clean white trousers. Soft moody background blur, high-contrast professional editing, hyper-realistic film texture, cinematic look, 4K resolution."
    },
    {
        "title": "2. Royal Golden Birthday Special Poster Trend", "type": "Trending",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000078737.jpg",
        "prompt": "Transform this image into a premium viral Instagram Birthday poster edit. Keep the subject's original face shape, eyes, lips, and smile completely unaltered. Layer 1 (Background): A massive close-up portrait of the person faded with elegant warm studio lights. Layer 2 (Foreground): A sharp full-body shot wearing an ultra-stylish outfit. The background is a beautiful rich abstract brown and golden watercolor paint stroke texture with realistic particle dust. Feature premium cursive typography text at the top reading 'HAPPY Birthday stylish pic'. Cinematic lighting, luxury aesthetic vibe, ultra HD."
    },
    {
        "title": "3. Instagram Viral Name Art Crown Edit (Aanya Style)", "type": "Trending",
        "image_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500",
        "prompt": "Create a viral CapCut trend overlay portrait. Keep the girl's original face structure and facial details 100% identical. The background is a dark, moody forest with orange and gold butterflies flying around. Combine a huge, faded close-up portrait of her wearing luxury sunglasses with a clear foreground shot. Above the foreground character, add clean, sharp typography text that reads 'Aanya' with a smaller subtitle 'Aanya editz' underneath, topped with a glowing minimalist golden crown icon. High fashion, cinematic lighting, 4K resolution."
    },
    {
        "title": "4. Instagram Viral Name Art Crown Edit (Arjun Style)", "type": "Trending",
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500",
        "prompt": "Create a trending Instagram Reels male portrait. Keep the original face, hair texture, and natural smile 100% identical. Dual exposure blend: a faded overhead close-up portrait combined with a sharp foreground shot. The background is an artistic dark grunge texture with dynamic golden bokeh sparkles. Feature bold, modern typography text above the shoulder reading 'ARJUN' and a stylized script text 'Arjun editz' below it with a royal crown vector element. Sharp focus, high contrast, cinematic poster look."
    },
    # --- BOYS HIGH-ENGAGEMENT PROMPTS ---
    {
        "title": "5. Neon Cyberpunk Dual Portrait Look", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500",
        "prompt": "Enhance this photo into a premium double exposure neon edit. Preserve the exact original face and facial hair of the boy completely. Background shows a giant, artistic, semi-transparent close-up of his original face with neon blue reflections. Foreground features his sharp full-body shot wearing a modern neon-accented techwear jacket, standing on a rainy street in Tokyo. Glowing cyan and pink lights, hyper-realistic texture, ultra-sharp focus, 8k resolution."
    },
    {
        "title": "6. Sunset Mountain Double Exposure Look", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1624561172888-ac93c696e10c?w=500",
        "prompt": "Transform this image. Keep the face, hair texture, and natural expressions 100% identical and original. Background features a magnificent, massive faded close-up portrait of his face overlapping a dramatic golden sunset and mountain peaks. Foreground shows him standing on a wooden deck in a stylish open dark shirt over a t-shirt. Moody warm color grading, cinematic atmosphere, 4K resolution."
    },
    {
        "title": "7. Patriotic Bhagat Singh Style Abstract Art", "type": "Boy",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000079586.jpg",
        "prompt": "Create a powerful, inspiring patriotic portrait from this photo. Modify the subject's outfit and styling to resemble the iconic revolutionary freedom fighter Bhagat Singh, wearing his classic vintage fedora hat and mustache. The subject's face shape and core features must remain completely recognizable and realistic. The background must be a striking, intense scarlet red dynamic abstract watercolor and ink sketch texture, with a bold silhouette of a raised fisted glove symbolizing strength. Cinematic lighting, 4K resolution masterwork."
    },
    {
        "title": "8. Vintage Retro Film Dual Edit", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=500",
        "prompt": "Modify this photo into a 90s retro cinematic poster. Face and skin details must remain 100% original. Background has a huge, artistic faded portrait of his face looking sideways with vintage sunglasses. Foreground shows him standing next to a vintage car in a cool oversized denim jacket. Warm nostalgic film grain, professional lighting, look like an aesthetic movie poster, 4k."
    },
    # --- GIRLS HIGH-ENGAGEMENT PROMPTS ---
    {
        "title": "9. Romantic K-Drama Rainy Day Aesthetic Hug", "type": "Girl",
        "image_url": "https://raw.githubusercontent.com/alammehtab4462-gif/mehtab-ai-app/main/1000079493.jpg",
        "prompt": "A beautiful cinematic wide shot of a romantic couple embracing tightly on a rainy evening at a nostalgic rural Japanese train station platform. The girl wears a stylish dark jacket and heels, and the boy wears a white button-up shirt and gray trousers. Lush green trees and small yellow flowers are visible along the platform edge. The atmosphere is filled with a soft rain mist, puddles reflecting the dim ambient station lights, and a moody, highly emotional blue-green cinematic color grade like a modern romance film."
    },
    {
        "title": "10. Cyberpunk Neon Queen Poster", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=500",
        "prompt": "Create a futuristic double exposure edit. Preserve the girl's exact original facial structure and smile. Background features a giant close-up profile of her face with glowing purple neon lighting lines. Foreground shows her in a sleek black leather outfit under rainy city neon signs. High-contrast color grading, photorealistic, cinematic edge, 4K resolution."
    },
    {
        "title": "11. Autumn Leaves Double Exposure Vibe", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500",
        "prompt": "Modify this photo into a warm aesthetic poster. Face must remain entirely original without changes. Background features a large, artistic faded portrait of her face gently blending with falling orange autumn leaves and a blurry forest path. Foreground displays her full figure wearing a cozy beige trench coat and a knitted scarf. Rich textures, moody soft lighting, ultra HD."
    },
    {
        "title": "12. Luxury Studio Vogue Style Dual Edit", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=500",
        "prompt": "Transform this photo into a professional high-fashion magazine cover layout. Keep the original face and skin texture completely untouched. Background displays a massive, high-contrast monochrome (black & white) faded close-up of her original face. Foreground shows her full-body pose in a vibrant luxury emerald green silk dress with dramatic soft-box studio lighting. Sharp focus, flawless professional design, 4K resolution."
    }
]

# Display Loop with Fallback Option
for item in prompts_data:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 4])
    with col1:
        if item['type'] == "Trending":
            st.markdown('<span class="tag-trending">🔥 Viral Trend</span>', unsafe_allow_html=True)
        elif item['type'] == "Boy":
            st.markdown('<span class="tag-boy">♂ Boy</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="tag-girl">♀ Girl</span>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"#### {item['title']}")
        
    try:
        st.image(item['image_url'], use_container_width=True)
    except:
        st.info("💡 Image preview is processing, look at the premium prompt below!")
        
    st.markdown("**📋 Copy Prompt:**")
    st.code(item['prompt'], language="text")
    st.markdown('</div>', unsafe_allow_html=True)
