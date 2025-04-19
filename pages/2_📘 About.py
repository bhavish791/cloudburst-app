import streamlit as st

st.set_page_config(page_title="About", page_icon="📘", layout="wide")

# 🌄 Background styling + main block
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://images.unsplash.com/photo-1508766206392-8bd5cf550d1d?auto=format&fit=crop&w=1740&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        [data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0);
        }
        .main-block {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        .app-header {
            background: linear-gradient(to right, #2193b0, #6dd5ed);
            padding: 1rem;
            border-radius: 12px;
            text-align: center;
            color: white;
            margin-bottom: 20px;
        }
        .app-header h1 {
            margin: 0;
            font-size: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Header (outside the content block)
st.markdown("""
    <div class="app-header">
        <h1>🌦️ Weather & Cloudburst App</h1>
    </div>
""", unsafe_allow_html=True)

# ✅ Main content inside a styled block
st.markdown('<div>', unsafe_allow_html=True)

st.title("📘 About This Project")

st.markdown("""
Welcome to the **Cloudburst Prediction and Weather App** built using **Streamlit**.

### 🌩️ Cloudburst Prediction
- Uses a machine learning model to detect high-risk weather.
- Inputs: Temperature, Apparent Temperature, Humidity, Wind Speed, Visibility, and Pressure.

### 🌍 Live Weather
- Real-time weather data from OpenWeatherMap.
- See temperature, wind, humidity, and get smart suggestions!

### 🛠️ Tech Stack
- Streamlit
- Python
- OpenWeatherMap API
- Machine Learning (Cloudburst Model)

---
Built with ❤️ for environmental safety and awareness.
""")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Footer remains
st.markdown("""
    <style>
        .footer {
            margin-top: 30px;
            padding: 1rem;
            text-align: center;
            color: white;
            background: linear-gradient(to right, #4b79a1, #283e51);
            border-radius: 12px;
            font-size: 0.9rem;
        }
        .footer a {
            color: #aadfff;
            text-decoration: none;
        }
    </style>
    <div class="footer">
        © 2025 <b>Weather App</b> | Built with ❤️ by <a href="https://github.com/your-username" target="_blank">Your Name</a> 
    </div>
""", unsafe_allow_html=True)
