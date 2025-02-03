import tkinter as tk
from tkinter import messagebox
import requests

# API Configuration
API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Entry for City Name
        self.city_label = tk.Label(self.root, text="Enter City Name:", font=("Arial", 12))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.city_entry.pack(pady=5)

        # Button to Fetch Weather
        self.get_weather_btn = tk.Button(self.root, text="Get Weather", command=self.fetch_weather, font=("Arial", 12))
        self.get_weather_btn.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), justify="left")
        self.result_label.pack(pady=10)

    def fetch_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        try:
            weather_data = self.get_weather_data(city)
            if weather_data:
                self.display_weather(weather_data)
            else:
                self.result_label.config(text="City not found. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def get_weather_data(self, city):
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for valid response
        if data["cod"] != 200:
            return None
        
        # Extracting and returning weather data
        weather_data = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "rain_chance": data.get("rain", {}).get("1h", 0),  # 1h rain chance if available
            "pressure": data["main"]["pressure"]
        }
        return weather_data

    def display_weather(self, weather):
        # Update the result label with weather information
        weather_info = (
            f"Temperature: {weather['temperature']}°C\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Wind Speed: {weather['wind_speed']} km/h\n"
            f"Rain Chance: {weather['rain_chance']}%\n"
            f"Pressure: {weather['pressure']} hPa"
        )
        self.result_label.config(text=weather_info)

# Main Application Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
