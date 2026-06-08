import streamlit as st
from datetime import datetime
import urllib.parse

# Page Configuration for Mobile View Look
st.set_page_config(page_title="Master Cutz Salon", page_icon="✂️", layout="centered")

# Custom Styling for Salon Look (Dark Gold & Luxury Black Theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #111827;
        color: #F3F4F6;
    }
    .salon-title {
        font-size: 28px;
        font-weight: 800;
        color: #F59E0B;
        text-align: center;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .salon-sub {
        font-size: 14px;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 25px;
    }
    .service-box {
        background-color: #1F2937;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #F59E0B;
        margin-bottom: 12px;
    }
    .whatsapp-btn {
        display: block;
        background-color: #25D366;
        color: white !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        margin-top: 15px;
        font-size: 16px;
    }
    .whatsapp-btn:hover {
        background-color: #128C7E;
    }
    .booking-success {
        background-color: #065F46;
        color: #34D399;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="salon-title">✂️ MASTER CUTZ SALON</div>', unsafe_allow_html=True)
st.markdown('<div class="salon-sub">Style Jo Aapko Sabse Alag Banaye | Book Your Slot</div>', unsafe_allow_html=True)

# Initialize database for Owner Dashboard (Register)
if "salon_bookings" not in st.session_state:
    st.session_state.salon_bookings = []

# DO DASHBOARD WAPAS LE AAYA HOON BHAI (Tabs)
tab1, tab2 = st.tabs(["📅 Book Appointment", "👑 Owner Dashboard"])

with tab1:
    st.markdown("### ✨ Hamari VIP Services")
    st.markdown('<div class="service-box"><b>💇‍♂️ Hair Cut (Trending Styles)</b><br>Price: ₹120 | Time: 20 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🧔 Beard Grooming & Styling</b><br>Price: ₹80 | Time: 15 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>💆‍♂️ Premium Hair Spa & Massage</b><br>Price: ₹250 | Time: 30 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🌟 Charcoal Facial & Glow</b><br>Price: ₹300 | Time: 25 Mins</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📝 Apni Details Bharein")

    customer_name = st.text_input("👤 Aapka Naam", placeholder="Apna pura naam likhein")
    customer_phone = st.text_input("📞 Mobile Number", placeholder="9876XXXXXX")

    selected_services = st.multiselect("✂️ Jo Service Chahiye Use Chunein", 
        ["Hair Cut (₹120)", "Beard Grooming (₹80)", "Hair Spa (₹250)", "Charcoal Facial (₹300)"])

    selected_barber = st.selectbox("💈 Apna Pasandida Karigar (Stylist) Chunein", [
        "Mubarak (Main Expert)",
        "Other Karigar 1",
        "Other Karigar 2",
        "Koi bhi chalega (Any Available)"
    ])

    booking_date = st.date_input("📆 Din Chunein", min_value=datetime.today())

    booking_time = st.selectbox("⏰ Apna Time Slot Chunein", [
        "09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM",
        "12:00 PM - 01:00 PM", "02:00 PM - 03:00 PM", "03:00 PM - 04:00 PM",
        "04:00 PM - 05:00 PM", "05:00 PM - 06:00 PM", "06:00 PM - 07:00 PM",
        "07:00 PM - 08:00 PM"
    ])

    st.markdown("---")

    # Owner Ka Number Set Hai
    owner_whatsapp_number = "918299250469" 

    if st.button("🔥 Booking Message Taiyar Karein", use_container_width=True):
        if not customer_name or not customer_phone or not selected_services:
            st.error("⚠️ Kripya Naam, Number aur Service zaroor chunein bhai!")
        else:
            # 1. Register me entry save karna
            services_string = ", ".join(selected_services)
            new_booking = {
                "name": customer_name,
                "phone": customer_phone,
                "services": services_string,
                "barber": selected_barber,
                "date": str(booking_date),
                "time": booking_time,
                "status": "Confirmed ✅"
            }
            st.session_state.salon_bookings.append(new_booking)
            
            # 2. WhatsApp message banana
            raw_message = (
                f"👋 *Master Cutz Salon - Nayi Booking!*\n\n"
                f"👤 *Customer Name:* {customer_name}\n"
                f"📞 *Phone:* {customer_phone}\n"
                f"✂️ *Services:* {services_string}\n"
                f"💈 *Karigar (Stylist):* {selected_barber}\n"
                f"📅 *Date:* {str(booking_date)}\n"
                f"⏰ *Time Slot:* {booking_time}\n\n"
                f"Kripya mera slot confirm karein! 🙏"
            )
            
            encoded_message = urllib.parse.quote(raw_message)
            whatsapp_url = f"https://wa.me/{owner_whatsapp_number}?text={encoded_message}"
            
            st.markdown(f'<div class="booking-success">🎉 Data Save Ho Gaya Hai!</div>', unsafe_allow_html=True)
            
            # Big Green WhatsApp Button
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">💬 Send Booking on WhatsApp</a>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 👑 Aaj Ki Kul Appointments (Dukaan Ka Register)")
    
    if len(st.session_state.salon_bookings) == 0:
        st.info("📭 Abhi tak koi nayi booking nahi hui hai bhai.")
    else:
        for idx, booking in enumerate(st.session_state.salon_bookings):
            st.markdown(f"""
            <div style="background-color: #1F2937; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #374151;">
                <h4>{idx+1}. {booking['name']} ({booking['time']})</h4>
                <p>📞 <b>Phone:</b> {booking['phone']}</p>
                <p>✂️ <b>Services:</b> {booking['services']}</p>
                <p>💈 <b>Karigar:</b> {booking['barber']}</p>
                <p>📅 <b>Date:</b> {booking['date']}</p>
                <p>🟢 <b>Status:</b> <span style="color: #34D399;">{booking['status']}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
        if st.button("🗑️ Reset Register (Clear All Bookings)", use_container_width=True):
            st.session_state.salon_bookings = []
            st.rerun()
