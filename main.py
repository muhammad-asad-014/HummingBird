# gui_only_weather_app.py

import streamlit as st
from HummingBird import getWeatherRecommendations

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="HummingBird AI - Weather Assistant", page_icon="🌤️", layout="centered")

# -----------------------------
# Title & Description
# -----------------------------
st.title("🌤️ HummingBird AI")
st.caption("Get real-time weather updates and AI-powered recommendations. Enter a city or detect your current location.")



weather = None



# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns([2, 1])

with col2:
    st.markdown("###  ")
    city = st.text_input("Enter City Name", placeholder="e.g., Lahore, Paris, Tokyo", key="city_input")
    if st.button("Get Weather Recommendations"):
        if city.strip() == "":
            st.warning("⚠️ Please enter a city name first.")
        else:
            # st.info(f"Fetching weather for: {city}")
            with st.spinner("Fetching weather data and generating AI recommendations..."):
                weather = getWeatherRecommendations(city)
                weather_recommendations = eval(weather[1])
    
    # st.markdown("---")
    # st.markdown("**Search History**")
    # st.write("- Lahore — 22°C, Clear Sky")
    # st.write("- Karachi — 30°C, Humid")
    # st.write("- Islamabad — 18°C, Cloudy")

with col1:
    # Placeholder weather card
    st.markdown("### Weather Overview")
    weather_card = st.container(border=True)
    with weather_card:
        colw1, colw2 = st.columns([1, 2])
        with colw1:
            st.image("https://openweathermap.org/img/wn/01d@4x.png", width=120)
        with colw2:
            if weather:
                print(weather)
                st.markdown(f"**{weather[0]['city']}**")
                st.markdown(f"☀️ {weather[0]['desc']}")
                st.metric(label="Temperature (°C)", value=f"{weather[0]['temp']}", delta="+2")
                st.metric(label="Feels Like", value=f"{weather[0]['feels_like']}°C")
                st.metric(label="Humidity", value=f"{weather[0]['humidity']}%")
            else:
                 with st.spinner("Fetching weather data and generating AI recommendations..."):
                    local_weather = getWeatherRecommendations()
                    local_weather_recommendations = eval(local_weather[1])
                    st.markdown(f"**{local_weather[0]['city']}**")
                    st.markdown(f"☀️ {local_weather[0]['desc']}")
                    st.metric(label="Temperature (°C)", value=f"{local_weather[0]['temp']}", delta="+2")
                    st.metric(label="Feels Like", value=f"{local_weather[0]['feels_like']}°C")
                    st.metric(label="Humidity", value=f"{local_weather[0]['humidity']}%")
                

    st.markdown("---")
    st.markdown("### 🧠 Personalized AI Recommendations")
    if weather:
        for recommendation in weather_recommendations:
            st.write(f"- {recommendation}")
    else:
        for recommendation in local_weather_recommendations:
            st.write(f"- {recommendation}")

    st.markdown("---")
    st.caption("Copyright 2025 • HummingBird AI • Developed by Asad")

# -----------------------------
# Footer Styling
# -----------------------------
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    .stButton button {
        background-color: #4B9CD3;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6em 1.2em;
        transition: 0.2s;
    }
    .stButton button:hover {
        background-color: #2C7DA0;
        transform: scale(1.02);
    }
    .stTextInput input {
        border-radius: 10px;
        border: 1px solid #ddd;
        padding: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
