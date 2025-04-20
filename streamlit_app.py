import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timezone

# Set page config FIRST
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Styled Header
st.markdown("""
    <style>
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
    <div class="app-header">
        <h1>🌦️ Weather & Cloudburst App</h1>
    </div>
""", unsafe_allow_html=True)

# --- Get user's city via IP ---
def get_user_city():
    try:
        response = requests.get("https://ipinfo.io")
        return response.json().get("city", "Mumbai")
    except:
        return "Mumbai"
    
    city = st.text_input("📍 Enter your city", placeholder="e.g., Delhi, New York", value="Dalles")


# --- Get current weather ---
def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        condition = data["weather"][0]["main"].lower()
        color_map = {
            "clear": "#FDF6EC",
            "clouds": "#ECECEC",
            "rain": "#D0E5F2",
            "thunderstorm": "#C7D2FE",
            "snow": "#F0F8FF",
            "mist": "#E8E8E8",
        }
        bg_color = color_map.get(condition, "#F9F9F9")
        return data, bg_color
    return None, "#FFFFFF"

# --- Hourly Forecast Function ---
def display_hourly_forecast(city, api_key, units="metric"):
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    res = requests.get(forecast_url)

    if res.status_code == 200:
        forecast_data = res.json()["list"][:8]  # 8x3hr = ~24h
        times = [datetime.fromtimestamp(item["dt"]).strftime("%I %p") for item in forecast_data]
        temps = [item["main"]["temp"] for item in forecast_data]
        humidity = [item["main"]["humidity"] for item in forecast_data]
        rain_chance = [item.get("pop", 0) * 100 for item in forecast_data]

        df = pd.DataFrame({
            "Time": times,
            "Temperature": temps,
            "Humidity": humidity,
            "Rain Probability": rain_chance
        })

        st.markdown("### 📊 Hourly Forecast (Next 24h)")
        fig = px.line(df, x="Time", y=["Temperature", "Humidity", "Rain Probability"], markers=True,
                      labels={"value": "Measurement", "Time": "Hour"},
                      title=f"Forecast: Temp (°C), Humidity (%) & Rain Probability (%)",
                      color_discrete_map={
                          "Temperature": "#FF5733",
                          "Humidity": "#33C1FF",
                          "Rain Probability": "#2ECC71"
                      })
        fig.update_traces(mode="lines+markers")
        fig.update_layout(hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Could not fetch hourly forecast.")

# --- Get user location & weather ---
API_KEY = st.secrets["weather"]["api_key"]
city = get_user_city()
weather_data, bg_color = get_weather_data(city, API_KEY)

# --- Dynamic Background ---
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_color};
    }}
    .home-title {{
        font-size: 36px;
        text-align: center;
        color: #003566;
        padding-bottom: 0.5em;
    }}
    .metric-box {{
        background-color: #ffffffaa;
        padding: 15px;
        border-radius: 12px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Intro Section ---
st.markdown("### 🚀 Features of the App")
st.markdown("""
- 🔮 **Cloudburst Prediction** using Machine Learning  
- 🌍 **Live Weather Forecasts** auto-detected by your location  
- 🧠 **Smart Weather Tips** based on conditions  
- 📰 **Latest Global Weather News**  
""")

# --- Show Weather Info ---
if weather_data:
    icon = weather_data["weather"][0]["icon"]
    desc = weather_data["weather"][0]["description"].title()

    st.markdown(f"### 📍 Weather in {city}")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.metric("Temperature", f"{weather_data['main']['temp']} °C")
        st.metric("Humidity", f"{weather_data['main']['humidity']} %")
        st.metric("Condition", desc)
        st.metric("Wind Speed", f"{weather_data['wind']['speed']} m/s")
    with col2:
        st.image(f"http://openweathermap.org/img/wn/{icon}@4x.png")

    # --- Show hourly forecast instead of 7-day ---
    display_hourly_forecast(city, API_KEY)
else:
    st.warning("Weather info not available.")

# --- Tips ---
st.markdown("### 💡 Smart Weather Tips")
st.success("🔋 Keep power banks charged during rainy season.")
st.info("📱 Enable location & alerts in weather apps.")
st.warning("🚗 Avoid waterlogged roads during heavy rains.")
st.info("🧴 Use sunscreen even on cloudy days.")

# --- News Section ---
NEWS_API_KEY = st.secrets["news"]["api_key"]
news_url = f"https://newsapi.org/v2/top-headlines?q=weather&language=en&pageSize=4&apiKey={NEWS_API_KEY}"
news_response = requests.get(news_url).json()

st.markdown("### 📰 Latest Weather News")
if "articles" in news_response:
    for article in news_response["articles"]:
        st.markdown(f"🔹 **[{article['title']}]({article['url']})**")
        if article.get("description"):
            st.caption(article["description"])
else:
    st.warning("🛑 Could not load news at the moment.")

# --- Footer ---
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
        © 2025 <b>Weather App</b> | Built with ❤️ by <a href="https://github.com/bhavish791" target="_blank">-3P.b-</a> 
    </div>
""", unsafe_allow_html=True)
