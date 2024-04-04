# CityRadar 
Python Mini Project

## Overview

This Python script provides information about the weather and top news headlines using OpenWeatherMap and NewsAPI. Additionally, a graphical user interface (GUI) has been added using Tkinter to enhance user interaction.

## Features

1. **Weather Information:**
   - Retrieves real-time weather data for a specified city using the OpenWeatherMap API.
   - Displays the city name, current weather conditions, temperature, and wind information.

2. **News Information:**
   - Fetches top headlines from the NewsAPI for the United States.
   - Displays title, description, publication date, and content for each news article.

3. **Graphical User Interface (Tkinter):**
   - Utilizes Tkinter to create a user-friendly GUI for interacting with the script.
   - Includes entry fields for entering the city name, a button to fetch data, and text areas for displaying weather and news information.

## How to Use

1. **Weather:**
   - Run the script.
   - Enter the desired city name in the Tkinter GUI when prompted.
   - View the retrieved weather information for the specified city.

2. **News:**
   - Run the script.
   - Get the latest top headlines from the NewsAPI for the United States in the Tkinter GUI.

3. **Graphical User Interface (Tkinter):**
   - Run the script.
   - Enter the city name and click the "Fetch Data" button to get weather and news information.
   - View the results in the Tkinter GUI text areas.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Configuration

### Weather API (OpenWeatherMap)

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) and replace the `api_key` variable in the script with your key.
2. The base URL for the OpenWeatherMap API is `"http://api.openweathermap.org/data/2.5/weather?"`.

### News API (NewsAPI.org)

1. Obtain an API key from [NewsAPI](https://newsapi.org/) and replace the `apiKey` variable in the script with your key.
2. The base URL for the NewsAPI is `"https://newsapi.org/v2/top-headlines?"`, and the `country` parameter is set to `"US"`.

## Usage

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script.
5. Use the Tkinter GUI to enter the city name and fetch weather and news information.
6. View the weather details and top news headlines.

## Note

- Ensure an active internet connection for accurate weather and news data retrieval.
- API keys are required for accessing weather and news data. Replace placeholder keys with your actual keys in the script.

## Collaborators

- [Anushka Korlapati](https://github.com/anushka-korlapati/)
- [Vikranth Udandarao](https://github.com/Vikranth3140/)
- [Swara Parekh](https://github.com/swara14/)
