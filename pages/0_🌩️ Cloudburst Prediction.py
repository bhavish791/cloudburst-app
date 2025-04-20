import streamlit as st
import pickle

#def prediction_page():

st.set_page_config(page_title="Cloudburst Prediction", page_icon="🌩️", layout="wide")

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
        <h1>🌩️ Cloudburst pridiction</h1>
        
    </div>
""", unsafe_allow_html=True)

# Page styling
page = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.postimg.cc/nct12YSX/bg-for-cb.jpg");
    background-size: cover;
    font-family: Arial, sans-serif;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
h1 {
    color: white;
    
}
h2, h3 {
    color: #FFD700;
}
</style>
"""
st.markdown(page, unsafe_allow_html=True)

# Load the pre-trained model
model = pickle.load(open("cbmodel.pkl", "rb"))



# App title
#st.title("🌩️ CloudBurst Prediction App")

# Inputs with Examples above each field
st.markdown("### Enter the Weather Parameters Below:")
st.markdown("_Example: Temperature (25.67890°C)_")
input_tem = st.number_input("Temperature (°C)", format="%.5f")

st.markdown("_Example: Apparent Temperature (28.12345°C)_")
input_atem = st.number_input("Apparent Temperature (°C)", format="%.5f")

st.markdown("_Example: Humidity (85%)_")
input_hum = st.number_input("Humidity (%)")

st.markdown("_Example: Wind Speed (12.3456 m/s)_")
input_ws = st.number_input("Wind Speed (m/s)", format="%.4f")

st.markdown("_Example: Wind Bearing (120°)_")
input_wb = st.number_input("Wind Bearing (°)")

st.markdown("_Example: Visibility (10.1234 km)_")
input_vis = st.number_input("Visibility (km)", format="%.4f")

st.markdown("_Example: Pressure (1013 hPa)_")
input_pre = st.number_input("Pressure (hPa)")

# Prepare input for prediction
pred = [[input_tem, input_atem, input_hum, input_ws, input_wb, input_vis, input_pre]]
result = model.predict(pred)

# Prediction logic
if st.button("Predict"):
    if result == 1:
        st.subheader("⚠️ **Alert: Cloudburst Predicted!**")
        st.markdown(
            """
            <div style="background-color: #9ACBD0; padding: 10px; border-radius: 8px; color: #2C3E50;">
            <h3>Precautions:</h3>
            <ul>
                <li>Avoid low-lying areas prone to flooding.</li>
                <li>Stay away from streams, rivers, and other bodies of water.</li>
                <li>Seek shelter in a sturdy building on higher ground.</li>
                <li>Keep emergency supplies ready, including flashlights, food, and water.</li>
                <li>Keep family and emergency contacts informed of your location.</li>
            </ul>
            <h3>Emergency Numbers:</h3>
            <ul>
                <li>Disaster Management Helpline: <b>108</b></li>
                <li>Police: <b>100</b></li>
                <li>Fire Brigade: <b>101</b></li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.subheader("✅ **No Cloudburst Predicted!**")
        st.markdown(
            """
            <div style="background-color: #D3F9D8; padding: 10px; border-radius: 8px; color: #1A1A1A">
            <h3>Observation:</h3>
            <p>Conditions seem normal; no immediate weather threat detected.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

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
