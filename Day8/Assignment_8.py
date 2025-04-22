from flask import Flask, render_template, request, jsonify
import os, random
import random
from datetime import datetime, timedelta


app = Flask(__name__)

def get_random_forecast(start_date):
    weather_descriptions = [
        ("23", "Breezy"),
        ("30", "Partly Cloudy"),
        ("28", "Mostly Cloudy"),
        ("34", "Mostly Sunny"),
        ("26", "Cloudy"),
        ("32", "Sunny"),
        ("12", "Rainy"),
        ("4", "Thunderstorms")
    ]
    forecast = []
    for i in range(10):
        code, text = random.choice(weather_descriptions)
        date = (start_date + timedelta(days=i))
        forecast.append({
            "code": code,
            "date": date.strftime("%d %b %Y"),
            "day": date.strftime("%a"),
            "high": str(random.randint(30, 40)),
            "low": str(random.randint(20, 30)),
            "text": text
        })
    return forecast

def generate_weather_data(city):
    return {
        "query": {
            "title": f"Weather - {city}",
            "location": {
                "city": city
            },
            "forecast": get_random_forecast(datetime(2025, 4, 21)),
           
        }
    }

@app.route("/")
@app.route("/<string:city>")
def weather_api(city = None):
    if city is not None:
        weather_data = {city: generate_weather_data(city)}
        data = jsonify(weather_data)
        return data
    else:
        return "<h1>Give a city Name in the path Parameter </h1>"
        
if __name__ == '__main__':
    app.run()
        
        
