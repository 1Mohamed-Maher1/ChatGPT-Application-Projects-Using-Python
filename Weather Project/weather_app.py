import tkinter as tk
from tkinter import messagebox, ttk
import requests

def get_weather():
    api_key = "YOUR_API_KEY"  
    city = city_entry.get().strip()  
    country_code = country_var.get().strip()  

    if not city:
        messagebox.showerror("Error", "Please enter a city")
        return

    location = f"{city},{country_code}"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", f"Location {location} not found!")
            return
        
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        precipitation = data["clouds"]["all"]

        temperature_label.config(text=f"{temperature}°C")
        humidity_label.config(text=f"{humidity}%")
        wind_speed_label.config(text=f"{wind_speed} km/h")
        pressure_label.config(text=f"{pressure} hPa")
        precipitation_label.config(text=f"{precipitation}%")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to get weather data.\n{e}")

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("300x300")

country_codes = ["EG", "US", "CA", "GB", "FR", "DE", "IT", "ES", "IN", "JP", "CN"]  

city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=20)
city_entry.insert(0, "Cairo")  
city_entry.pack()

country_var = tk.StringVar(root)
country_var.set("EG")  
country_label = tk.Label(root, text="Select Country Code:")
country_label.pack(pady=5)
country_dropdown = ttk.Combobox(root, textvariable=country_var, values=country_codes)
country_dropdown.pack()

search_button = tk.Button(root, text="Search", command=get_weather)
search_button.pack(pady=10)

temperature_label = tk.Label(root, text="Temperature: --°C", font=("Arial", 10))
temperature_label.pack()
humidity_label = tk.Label(root, text="Humidity: --%", font=("Arial", 10))
humidity_label.pack()
wind_speed_label = tk.Label(root, text="Wind Speed: -- km/h", font=("Arial", 10))
wind_speed_label.pack()
pressure_label = tk.Label(root, text="Pressure: -- hPa", font=("Arial", 10))
pressure_label.pack()
precipitation_label = tk.Label(root, text="Precipitation: --%", font=("Arial", 10))
precipitation_label.pack()

root.mainloop()
