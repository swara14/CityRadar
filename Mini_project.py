import requests
import json

def get_weather(api_key, city_name, temperature_unit='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units={temperature_unit}"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx status codes)
        weather_data = response.json()

        print("City:", weather_data["name"])
        print("Weather:", weather_data["weather"][0]["description"])
        print("Temperature:", weather_data["main"]["temp"], "°C")
        print("Wind Speed:", weather_data["wind"]["speed"], "m/s")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

def get_news(api_key):
    url = 'https://newsapi.org/v2/top-headlines?' 'country=us&' f'apiKey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        articles = news_data['articles']
        for index, article in enumerate(articles, start=1):
            print('------------------------------------------')
            print('\n' + f"Title {index}")
            print(article['title'])
            print('\n' + f"Description {index}")
            print(article['description'])
            print('\n' + f"Published on {index}")
            print(article['publishedAt'])
            print('\n' + f"Content {index}")
            print(article['content'])
            print('------------------------------------------')

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

def main():
    api_key_weather = "1c4aaa597dd29ba9c44da6839c89fbf6"
    api_key_news = "a3219de17f424b1380562001868597fe"

    if not api_key_weather or not api_key_news:
        print("Please provide API keys.")
        return

    city_name = input("Enter city name: ")
    temperature_unit = input("Enter temperature unit (default is Celsius, enter 'imperial' for Fahrenheit): ")

    if temperature_unit.lower() not in ['metric', 'imperial']:
        temperature_unit = 'metric'

    get_weather(api_key_weather, city_name, temperature_unit)
    print()
    get_news(api_key_news)

if __name__ == "__main__":
    main()