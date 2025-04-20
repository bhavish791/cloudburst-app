import streamlit as st
import requests
from datetime import datetime
import folium
from streamlit_folium import st_folium
import pandas as pd
import plotly.express as px

# Inside 1_Weather_App.py
st.set_page_config(page_title="Weather Lookup", page_icon="🌤️")


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
        .app-header p {
            margin: 0;
            font-size: 1rem;
            opacity: 0.9;
        }
    </style>
    <div class="app-header">
        <h1>🌦️ Weather info</h1>
        
    </div>
""", unsafe_allow_html=True)

# API
API_KEY = st.secrets["weather"]["api_key"]

# Input
unit = st.radio("Choose Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
units = "metric" if unit.startswith("C") else "imperial"
symbol = "°C" if units == "metric" else "°F"

city = st.text_input("📍 Enter a city", placeholder="e.g., Delhi, New York")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]
        main = data["main"]
        wind = data["wind"]
        sys = data["sys"]
        coord = data["coord"]
        icon = weather["icon"]
        desc = weather["description"]

        # Weather-based background color
        bg = "#DFF6FF" if "clear" in desc else "#FCE2DB" if "rain" in desc else "#EDEDED"
        st.markdown(f"<style>.stApp {{background-color: {bg};}}</style>", unsafe_allow_html=True)

        sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(sys["sunset"]).strftime('%H:%M:%S')

        st.title(f"🌤️ Weather in {city.title()}")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
                <div style="background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                    <h3>{weather['main']} - {desc.title()}</h3>
                    <p><b>Temperature:</b> {main['temp']} {symbol}</p>
                    <p><b>Feels Like:</b> {main['feels_like']} {symbol}</p>
                    <p><b>Humidity:</b> {main['humidity']}%</p>
                    <p><b>Pressure:</b> {main['pressure']} hPa</p>
                    <p><b>Wind:</b> {wind['speed']} m/s</p>
                    <p><b>Sunrise:</b> {sunrise}</p>
                    <p><b>Sunset:</b> {sunset}</p>
                </div>
            """, unsafe_allow_html=True)

            # Suggestions
            if "rain" in desc:
                st.warning("☔ Carry an umbrella!")
            elif "clear" in desc:
                st.success("☀️ Great weather today!")
            elif "cloud" in desc:
                st.info("☁️ A little cloudy.")
            elif "snow" in desc:
                st.warning("❄️ Dress warmly!")
        with col2:
            st.image(f"http://openweathermap.org/img/wn/{icon}@4x.png")

        # Hourly Forecast Chart (Next 8 entries ~ 24 hours)
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}"
        forecast_response = requests.get(forecast_url)

        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()["list"][:8]
            times = [datetime.fromtimestamp(item["dt"]).strftime("%I %p") for item in forecast_data]
            temps = [item["main"]["temp"] for item in forecast_data]
            humidity = [item["main"]["humidity"] for item in forecast_data]
            rain_chance = [item.get("pop", 0) * 100 for item in forecast_data]  # 'pop' is probability of precipitation

            df = pd.DataFrame({
                "Time": times,
                "Temperature": temps,
                "Humidity": humidity,
                "Rain Probability": rain_chance
            })

            st.subheader("📊 Hourly Forecast (Next 24h)")
            fig = px.line(df, x="Time", y=["Temperature", "Humidity", "Rain Probability"], markers=True,
                          labels={"value": "Measurement", "Time": "Hour"},
                          title=f"Forecast: Temperature ({symbol}), Humidity (%) & Rain Probability (%)",
                          color_discrete_map={
                              "Temperature": "#FF5733",
                              "Humidity": "#33C1FF",
                              "Rain Probability": "#2ECC71"
                          })
            fig.update_traces(mode="lines+markers")
            fig.update_layout(hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error("Couldn't fetch hourly forecast.")

    else:
        st.error("City not found.")

#-------------MAP-----------------------------
if city and response.status_code == 200:
    st.markdown("### 🗺️ Interactive Weather Map")
    lat, lon = coord["lat"], coord["lon"]

    # Create base map
    m = folium.Map(location=[lat, lon], zoom_start=7)

    # Dictionary of tile types
    overlay_types = {
        "Clouds": "clouds_new",
        "Precipitation": "precipitation_new",
        "Temperature": "temp_new",
        "Wind": "wind_new",
        "Pressure": "pressure_new"
    }

    # Add each overlay
    for name, tile in overlay_types.items():
        tile_url = f"https://tile.openweathermap.org/map/{tile}/{{z}}/{{x}}/{{y}}.png?appid={API_KEY}"
        folium.TileLayer(
            tiles=tile_url,
            name=name,
            attr="OpenWeatherMap",
            overlay=True,
            control=True
        ).add_to(m)

    # Add city marker
    folium.Marker(
        location=[lat, lon],
        tooltip=f"{city.title()}",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # Add layer control
    folium.LayerControl(collapsed=False).add_to(m)

    # Display map in Streamlit
    st_data = st_folium(m, width=700, height=450)
    
    # Styled Footer
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
        © 2025 <b>Weather App</b> | Built with ❤️ by <a href="https://github.com/your-username" target="_blank">-3P.b-</a> 
    </div>
""", unsafe_allow_html=True)
