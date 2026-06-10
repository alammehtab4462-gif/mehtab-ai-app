import streamlit as st
from datetime import datetime
import urllib.parse
import json
import os

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
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .salon-owner {
        font-size: 16px;
        font-weight: 600;
        color: #E5E7EB;
        text-align: center;
        margin-bottom: 5px;
        font-style: italic;
        letter-spacing: 1px;
    }
    .salon-sub {
        font-size: 13px;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 18px;
        font-weight: bold;
        color: #F59E0B;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 2px solid #F59E0B;
        padding-bottom: 5px;
        text-transform: uppercase;
    }
    .service-box {
        background-color: #1F2937;
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #F59E0B;
        margin-bottom: 8px;
    }
    .offer-box {
        background-color: #292524;
        padding: 12px;
        border-radius: 8px;
        border: 1px dashed #F59E0B;
        margin-bottom: 8px;
        text-align: center;
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

# File to store data permanently on server
DB_FILE = "bookings_db.json"

# Helper functions to handle permanent database
def load_bookings():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_booking(new_data):
    current_bookings = load_bookings()
    current_bookings.append(new_data)
    with open(DB_FILE, "w") as f:
        json.dump(current_bookings, f, indent=4)

def clear_all_bookings():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

# Header Section
st.markdown('<div class="salon-title">✂️ MASTER CUTZ SALON</div>', unsafe_allow_html=True)
st.markdown('<div class="salon-owner">Owned by Khan Sahab</div>', unsafe_allow_html=True)
st.markdown('<div class="salon-sub">Style That Makes You Stand Out | Book Your Slot</div>', unsafe_allow_html=True)

# Tabs Configuration
tab1, tab2 = st.tabs(["📅 Book Appointment", "👑 Owner Dashboard"])

with tab1:
    # 1. Standard Services Menu
    st.markdown('<div class="section-header">📜 Our Menu & Price List</div>', unsafe_allow_html=True)
    
    services_list = [
        "Classic Hair Cut (₹100)", "Beard / Shave (₹50)", "Hair Wash (₹30)", 
        "Clean Up (₹50)", "Hair Dryer (₹30)", "Hair / Beard Color (₹250)", 
        "Keratin / Hair Spa (₹500)", "Keratin / Hair Spa (₹900)", 
        "Head / Body Massage (₹100)", "D Tan (₹150)", "D Tan (₹250)", 
        "Facial (₹600)", "Facial (₹1100)", "Special Hair Color (₹800)", 
        "Hair Straightening (₹1200)", "Wax (₹150)", "Wax (₹250)", 
        "Wax Beard (₹100)", "Wax Beard (₹150)"
    ]
    
    st.markdown('<div class="service-box"><b>💇‍♂️ Hair & Beard Basics</b><br>Classic Hair Cut: ₹100 | Beard/Shave: ₹50 | Hair Wash: ₹30</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🌟 Grooming & Spa</b><br>Clean Up: ₹50 | Hair Spa: ₹500/₹900 | Facial: ₹600/₹1100</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🔥 Styling & Colors</b><br>Hair Color: ₹250 | Special Color: ₹800 | Straightening: ₹1200</div>', unsafe_allow_html=True)

    # 2. Mastercutz Special Combos
    st.markdown('<div class="section-header">⭐ Mastercutz Special Combos</div>', unsafe_allow_html=True)
    combos_list = [
        "Combo 1: Hair + Beard + D Tan + Head Massage (₹350)",
        "Combo 2: Hair + Beard + D Tan + Head Massage (₹450)",
        "Combo 3: Hair Cut + Beard Cut + Color (₹350)",
        "Combo 4: Hair Cut + Beard Cut + Color + D Tan (₹500)"
    ]
    st.markdown('<div class="service-box"><b>🎁 Hair/Beard/D Tan/Head Massage</b><br>Price: ₹350 / ₹450</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🎁 Hair Cut + Beard Cut + Color</b><br>Price: ₹350</div>', unsafe_allow_html=True)
    st.markdown('<div class="service-box"><b>🎁 Hair Cut + Beard Cut + Color + D Tan</b><br>Price: ₹500</div>', unsafe_allow_html=True)

    # 3. Special Offers Display
    st.markdown('<div class="section-header">💥 Special Offers Only for You</div>', unsafe_allow_html=True)
    st.markdown('<div class="offer-box"><b style="color: #F59E0B; font-size: 16px;">📅 ONLY TUESDAY OFFER</b><br><span style="font-size: 20px; font-weight: bold; color: #34D399;">20% OFF</span> ON TOTAL BILL</div>', unsafe_allow_html=True)
    st.markdown('<div class="offer-box"><b style="color: #F59E0B; font-size: 16px;">🤵 GROOM SPECIAL OFFER</b><br>Complete Package for <span style="font-size: 18px; font-weight: bold; color: #34D399;">₹2000/- Only</span></div>', unsafe_allow_html=True)

    all_options = services_list + combos_list + ["ONLY TUESDAY OFFER (20% OFF)", "GROOM SPECIAL OFFER (₹2000)"]

    st.markdown('<div class="section-header">📝 Enter Your Details</div>', unsafe_allow_html=True)

    customer_name = st.text_input("👤 Full Name", placeholder="Enter your full name here")
    customer_phone = st.text_input("📞 Mobile Number", placeholder="Enter 10-digit mobile number")

    selected_services = st.multiselect("✂️ Choose Services / Combos / Offers", all_options)

    selected_barber = st.selectbox("💈 Select Your Stylist (Karigar)", [
        "Mubarak",
        "Other Stylist 1",
        "Other Stylist 2",
        "Any Available"
    ])

    booking_date = st.date_input("📆 Select Date", min_value=datetime.today())

    booking_time = st.selectbox("⏰ Select Time Slot", [
        "09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM",
        "12:00 PM - 01:00 PM", "02:00 PM - 03:00 PM", "03:00 PM - 04:00 PM",
        "04:00 PM - 05:00 PM", "05:00 PM - 06:00 PM", "06:00 PM - 07:00 PM",
        "07:00 PM - 08:00 PM"
    ])

    st.markdown("---")

    owner_whatsapp_number = "918299250469" 

    if st.button("🔥 Generate Booking Message", use_container_width=True):
        if not customer_name or not customer_phone or not selected_services:
            st.error("⚠️ Please fill in your Name, Phone, and choose at least one Service!")
        else:
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
            
            # Permanently save data to server file
            save_booking(new_booking)
            
            raw_message = (
                f"👋 *Master Cutz Salon - New Booking!*\n\n"
                f"👤 *Customer Name:* {customer_name}\n"
                f"📞 *Phone:* {customer_phone}\n"
                f"✂️ *Selected Items:* {services_string}\n"
                f"💈 *Stylist (Karigar):* {selected_barber}\n"
                f"📅 *Date:* {str(booking_date)}\n"
                f"⏰ *Time Slot:* {booking_time}\n\n"
                f"Please confirm my booking slot! 🙏"
            )
            
            encoded_message = urllib.parse.quote(raw_message)
            whatsapp_url = f"https://wa.me/{owner_whatsapp_number}?text={encoded_message}"
            
            st.markdown(f'<div class="booking-success">🎉 Data Saved Successfully!</div>', unsafe_allow_html=True)
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">💬 Send Booking on WhatsApp</a>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 👑 Today's Appointments (Permanent Salon Register)")
    
    # Load bookings from file storage
    saved_bookings = load_bookings()
    
    if len(saved_bookings) == 0:
        st.info("📭 No new bookings for today yet.")
    else:
        for idx, booking in enumerate(saved_bookings):
            st.markdown(f"""
            <div style="background-color: #1F2937; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #374151;">
                <h4>{idx+1}. {booking['name']} ({booking['time']})</h4>
                <p>📞 <b>Phone:</b> {booking['phone']}</p>
                <p>✂️ <b>Services/Offers:</b> {booking['services']}</p>
                <p>💈 <b>Stylist:</b> {booking['barber']}</p>
                <p>📅 <b>Date:</b> {booking['date']}</p>
                <p>🟢 <b>Status:</b> <span style="color: #34D399;">{booking['status']}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
        if st.button("🗑️ Reset Register (Clear All Bookings)", use_container_width=True):
            clear_all_bookings()
            st.success("🧹 Register has been successfully cleared!")
            st.rerun()
 file contents here
