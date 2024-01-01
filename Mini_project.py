import requests
import json
import tkinter as tk
from tkinter import Scrollbar, Text, messagebox

def get_weather(city_name):
    api_key = "1c4aaa597dd29ba9c44da6839c89fbf6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()

def display_weather(weather_data):
    info = (f"City: {weather_data['name']}\n"
            f"Weather: {weather_data['weather'][0]['description']}\n"
            f"Temperature: {weather_data['main']['temp']} Kelvin\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s")
    return info

def get_news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=a3219de17f424b1380562001868597fe')
    response = requests.get(url)
    return response.json()

def display_news(news_data):
    articles = news_data['articles']
    news_info = "GENERAL NEWS HEADLINES:\n-------------------\n"
    for i, article in enumerate(articles, 1):
        news_info += (f"\nTitle {i}: {article['title']}\n"
                      f"Description {i}: {article['description']}\n"
                      f"Published on {i}: {article['publishedAt']}\n"
                      f"Content {i}: {article['content']}\n"
                      '------------------------------------------\n')
    return news_info

def fetch_data(city_entry, weather_text, news_text):
    city_name = city_entry.get()
    if not city_name:
        messagebox.showinfo("Error", "Please enter a city name.")
        return

    # Get and display weather information
    weather_data = get_weather(city_name)
    weather_info = display_weather(weather_data)
    weather_text.delete(1.0, tk.END)
    weather_text.insert(tk.END, weather_info)

    # Get and display news headlines
    news_data = get_news()
    news_info = display_news(news_data)
    news_text.delete(1.0, tk.END)
    news_text.insert(tk.END, news_info)

# Create the main GUI window
root = tk.Tk()
root.title("Weather and News App")

# Set background image
background_image = tk.PhotoImage(file="city_background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place widgets
city_label = tk.Label(root, text="Enter city name:", font=('Helvetica', 14, 'bold'), bg='white')
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Data", command=lambda: fetch_data(city_entry, weather_text, news_text), font=('Helvetica', 12, 'bold'), bg='#4CAF50', fg='white')
fetch_button.pack(pady=10)

weather_text = Text(root, height=8, width=50, wrap=tk.WORD, font=('Helvetica', 12), bg='#87CEEB')
weather_text.pack(pady=5)

news_text = Text(root, height=15, width=50, wrap=tk.WORD, font=('Helvetica', 12), bg='#FFD700')
news_text.pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()