https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=500",
        "prompt": "Enhance this photo. Keep the person's exact original face shape, facial features, expressions, and skin tone 100% unchanged. Modify only the background and clothing: place him on a futuristic Tokyo street at night with glowing blue and purple neon lights, light rain reflections on the ground. Change his outfit to a premium black techwear cyberpunk jacket. High-end cinematic lighting, ultra-realistic, 4K resolution, photorealistic."
    },
    {
        "title": "2. Royal Indian Ethnic Look", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500",
        "prompt": "Enhance this photo. Do not alter the face, eyes, lips, or hair features of the original person. Keep the face 100% original. Change the attire to a rich luxury gold and maroon embroidered Sherwani. Change the background to a grand royal palace hallway with soft warm chandelier lighting and elegant pillars. Masterpiece, ultra-sharp detail, 4K quality."
    },
    {
        "title": "3. Luxury CEO Executive Vibe", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500",
        "prompt": "Enhance this photo. Keep the original face and skin textures completely intact without any changes. Alter the background to a high-end luxury corporate office overlooking a skyscraper city skyline at sunset. Dress the person in a perfectly tailored dark charcoal grey slim-fit tuxedo with a crisp white shirt. Professional corporate studio lighting, 8k resolution, sharp focus."
    },
    {
        "title": "4. Cinematic Desert Rider Look", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1624561172888-ac93c696e10c?w=500",
        "prompt": "Enhance this photo. Maintain the original face, facial hair, and look of the person completely. Place him in a scenic golden hour desert landscape next to a vintage cafe racer motorcycle. Outfit changed to a rugged premium brown leather jacket over a black t-shirt. Dramatic cinematic sun rays, hyper-realistic texture, 4K resolution."
    },
    {
        "title": "5. Vintage Retro 90s Aesthetic", "type": "Boy",
        "image_url": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500",
        "prompt": "Enhance this photo. The face must remain entirely original and unchanged. Change the setting to a retro 1990s aesthetic street cafe with vintage cars blurred in the background. Dress the person in a stylish oversized vintage denim jacket. Soft nostalgic film grain effect, warm color grading, cinematic editorial portrait style, ultra HD."
    },
    {
        "title": "6. Angelic Fairy White Gown Look", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500",
        "prompt": "Enhance this photo. Keep the girl's original face, eyes, facial structure, and smile 100% identical and unchanged. Change only the surroundings and outfit: dress her in a breathtaking, glowing white luxury fairy gown. Place her in an enchanted magical forest background with soft glowing fireflies and golden light rays filtering through ancient trees. Soft focus, ethereal cinematic lighting, 4K resolution."
    },
    {
        "title": "7. Royal Traditional Lehenga Look", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500",
        "prompt": "Enhance this photo. Keep the face, skin tone, and expressions completely original without any modifications. Dress her in a majestic, highly-detailed royal emerald green and gold embroidered bridal Lehenga with elegant traditional jewelry. The background should be a luxury heritage palace balcony during a grand evening event with soft bokeh lights. High-end fashion photography, 8k resolution."
    },
    {
        "title": "8. Modern Luxury Street Fashion", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500",
        "prompt": "Enhance this photo. Preserve the exact original face and natural features of the girl. Change the outfit to a chic high-fashion beige trench coat with a modern black turtleneck sweater. Place her on a classy street in Paris with the Eiffel tower beautifully blurred in the background. Magazine cover style lighting, photorealistic, sharp details, 4K."
    },
    {
        "title": "9. Cyber-Princess Neon Cyberpunk", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=500",
        "prompt": "Enhance this photo. Do not alter the girl's original face, expressions, or features. Modify the outfit into a futuristic sleek black and glowing pink cybernetic jacket. Background is a neon-lit cyberpunk city rooftop at night with futuristic drones and neon glowing advertisements blurred in the distance. Cinematic dynamic lighting, ultra HD, hyper-detailed."
    },
    {
        "title": "10. Cozy Autumn Coffee Shop Aesthetic", "type": "Girl",
        "image_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=500",
        "prompt": "Enhance this photo. The original face and natural skin textures must be kept 100% unchanged. Change the setting to a beautiful, cozy indoor coffee shop next to a rain-covered glass window with autumn leaves outside. Dress her in a soft, premium oversized woolen knitted sweater holding a steaming coffee mug. Warm moody lighting, beautiful bokeh, photorealistic, 4K."
    }
]

# Display
for item in prompts_data:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 4])
    with col1:
        if item['type'] == "Boy":
            st.markdown('<span class="tag-boy">♂ Boy</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="tag-girl">♀ Girl</span>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"#### {item['title']}")
        
    st.image(item['image_url'], use_container_width=True)
    st.markdown("**📋 Copy Prompt:**")
    st.code(item['prompt'], language="text")
    st.markdown('</div>', unsafe_allow_html=True)
