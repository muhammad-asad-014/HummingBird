# 🌤️ HummingBird AI — Smart Weather Assistant

[![Streamlit App](https://img.shields.io/badge/Launch_App-Streamlit-brightgreen?logo=streamlit)](https://hummingbird-ai.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> ✨ Your AI-powered companion for real-time weather insights, travel suggestions, and activity recommendations — all in one elegant Streamlit interface.

---

## 🚀 Live Demo
🌍 **Try it now:** [https://hummingbird-ai.streamlit.app/](https://hummingbird-ai.streamlit.app/)

---

## 🧠 Overview
**HummingBird AI** combines real-time weather data with intelligent AI-driven insights.  
You can **enter any city name** or let the app **auto-detect your current location** using IP geolocation.  
The app fetches **live weather updates** from the OpenWeather API (or free alternatives) and sends the data to an AI model for **personalized recommendations** — whether it’s what to wear, when to travel, or what outdoor activities suit the day.

---

## ✨ Features

| Category | Description |
|-----------|-------------|
| 🌦️ **Real-Time Weather** | Fetch current temperature, humidity, feels-like, and conditions from OpenWeather. |
| 📍 **Smart Location Detection** | Get weather for your current city automatically via IP-based geolocation. |
| 🧠 **AI-Powered Insights** | Uses Google Gemini (or compatible LLM) to recommend clothing, outdoor activities, and travel advice. |
| 🪶 **Elegant Streamlit UI** | Designed with responsive layout, smooth loaders, and beautiful cards. |
| 🔒 **Secure API Usage** | API keys stored safely with `.env` and `python-dotenv`. |
| ⚙️ **Error Handling** | Graceful fallbacks for invalid city names, no internet, or API limits. |

---


## 🧩 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (for the interactive GUI)
- **Backend:** Python (with `requests`, `geocoder`, and `dotenv`)
- **AI Model:** Google Gemini / OpenAI GPT (for generating recommendations)
- **Weather API:** OpenWeatherMap (can be swapped for Open-Meteo for unlimited free usage)
- **Deployment:** [Streamlit Cloud](https://streamlit.io/cloud)

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/hummingbird-ai.git
cd hummingbird-ai
