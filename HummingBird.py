from openai import OpenAI
import os
from dotenv import load_dotenv
import geocoder
load_dotenv()




def getWeather(city="lahore", api_key = None):
    import requests
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" }
    try:
        response = requests.get(base_url, params=params)
        if response.json()['cod']!=200:
            return "Error occurred! Please try again"
        else:
            x = response.json()['main']
            x['desc'] = response.json()['weather'][0]['description']
            x['city'] = city.capitalize()
            return x
    except Exception as e:
        print(f"ERROR!: {e}")



def getWeatherRecommendations(city = geocoder.ip("me").city):

    curr_weather = getWeather(city= city, api_key=os.getenv("Open_Weather_API_KEY"))
    client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    try:
        completion = client.chat.completions.create(
        extra_body={},
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": """You are an AI weather assistant, You will be given the weather information of a city and you will respond in a python list containing five recommendations based on the provided weather data such as clothing, travel, or activity suggestions. The output should be only a list like this format ['Light, breathable clothing with a wind‑breathable jacket for a breeze‑free walk in Lahore today.',
 'Carry a reusable water bottle and sip often; 64% humidity means you’ll perspire more.',
 'Wear a quality face mask or cover to reduce inhalation of smoke particles while stepping outside.',
 'Plan indoor activities like visiting a museum or a reading nook to avoid smoke exposure and keep cool.',
 'Schedule outdoor exercise outside peak sun hours (early morning or late evening) and use sunscreen with at least SPF 30.']. Don't use such characters which python cannot process such as invalid character '‑' (U+2011) or any other characters like this"""
            },
            {
                "role": "user",
                "content": f"{curr_weather}"
            }
        ]
        )
        result = [curr_weather, completion.choices[0].message.content]
        return(result)
    except Exception as e:
        print(e)
        return(e)     




