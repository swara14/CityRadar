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
    news_info = "HEADLINES:\n-------------------\n"
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


    weather_data = get_weather(city_name)
    weather_info = display_weather(weather_data)
    weather_text.delete(1.0, tk.END)
    weather_text.insert(tk.END, weather_info)

    
    news_data = get_news()
    news_info = display_news(news_data)
    news_text.delete(1.0, tk.END)
    news_text.insert(tk.END, news_info)


root = tk.Tk()
root.title("Weather and News App")


city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Data", command=lambda: fetch_data(city_entry, weather_text, news_text))
fetch_button.pack()

weather_text = Text(root, height=10, width=50)
weather_text.pack()

news_text = Text(root, height=15, width=50)
news_text.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
