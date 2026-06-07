import streamlit as st
from datetime import datetime

# Page Configuration for Mobile View Look
st.set_page_config(page_title="Premium Salon Booking", page_icon="✂️", layout="centered")

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
st.markdown('<div class="salon-title">✂️ MEHTAB PREMIUM SALON</div>', unsafe_allow_html=True)
st.markdown('<div class="salon-sub">Style Jo Aapko Sabse Alag Banaye | Book Your Slot</div>', unsafe_allow_html=True)

# Initialize a fake database in system memory to store appointments
if "salon_bookings" not in st.session_state:
    st.session_state.salon_bookings = []

# Create Tabs for Customer Booking and Owner Dashboard
tab1, tab2 = st.tabs(["📅 Book Appointment", "👑 Owner Dashboard (Dukaan Ke Liye)"])

with tab1:
    st.markdown("### ✨ Hamari VIP Services")
    
    # Displaying Services Beautifully
    st.markdown('<div class="service-box"><b>💇‍♂️ Hair Cut (Trending Styles)</b><br>Price: ₹120 | Time: 20 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🧔 Beard Grooming & Styling</b><br>Price: ₹80 | Time: 15 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>💆‍♂️ Premium Hair Spa & Massage</b><br>Price: ₹250 | Time: 30 Mins</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🌟 Charcoal Facial & Glow</b><br>Price: ₹300 | Time: 25 Mins</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📝 Apni Details Bharein")
    
    # Booking Form
    customer_name = st.text_input("👤 Aapka Naam", placeholder="Apna pura naam likhein")
    customer_phone = st.text_input("📞 Mobile Number", placeholder="9876XXXXXX")
    
    selected_services = st.multiselect("✂️ Jo Service Chahiye Use Chunein", 
        ["Hair Cut (₹120)", "Beard Grooming (₹80)", "Hair Spa (₹250)", "Charcoal Facial (₹300)"])
    
    booking_date = st.date_input("📆 Din Chunein", min_value=datetime.today())
    
    booking_time = st.selectbox("⏰ Apna Pasandida Time Slot Chunein", [
        "09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM",
        "12:00 PM - 01:00 PM", "02:00 PM - 03:00 PM", "03:00 PM - 04:00 PM",
        "04:00 PM - 05:00 PM", "05:00 PM - 06:00 PM", "06:00 PM - 07:00 PM",
        "07:00 PM - 08:00 PM"
    ])
    
    book_btn = st.button("🔥 Confirm VIP Booking", use_container_width=True)
    
    if book_btn:
        if not customer_name or not customer_phone or not selected_services:
            st.error("⚠️ Kripya Naam, Number aur Service zaroor chunein bhai!")
        else:
            # Save booking info
            new_booking = {
                "name": customer_name,
                "phone": customer_phone,
                "services": ", ".join(selected_services),
                "date": str(booking_date),
                "time": booking_time,
                "status": "Confirmed ✅"
            }
            st.session_state.salon_bookings.append(new_booking)
            st.markdown(f'<div class="booking-success">🎉 Badhai Ho {customer_name}! Aapka Slot ({booking_time}) Confirm Ho Gaya Hai. Time Par Pahunchein!</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 👑 Aaj Ki Kul Appointments (Dukaan Ka Register)")
    st.write("Yeh section sirf aapke dost ke liye hai, jahan wo dekh sakte hain kis customer ka booking kab hai.")
    
    if len(st.session_state.salon_bookings) == 0:
        st.info("📭 Abhi tak koi naya appointment book nahi hua hai bhai.")
    else:
        for idx, booking in enumerate(st.session_state.salon_bookings):
            st.markdown(f"""
            <div style="background-color: #1F2937; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #374151;">
                <h4>{idx+1}. {booking['name']} ({booking['time']})</h4>
                <p>📞 <b>Phone:</b> {booking['phone']}</p>
                <p>✂️ <b>Services:</b> {booking['services']}</p>
                <p>📅 <b>Date:</b> {booking['date']}</p>
                <p>🟢 <b>Status:</b> <span style="color: #34D399;">{booking['status']}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
        if st.button("🗑️ Reset Register (Clear All Bookings)", use_container_width=True):
            st.session_state.salon_bookings = []
            st.rerun()
