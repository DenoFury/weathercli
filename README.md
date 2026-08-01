# Weather Dashboard CLI

A command-line tool that fetches real-time weather data for any city and logs each lookup to a CSV file, building a simple history over time.

## Features
- Look up current weather for any city by name
- Converts city name to coordinates using a free geocoding API
- Displays temperature and current conditions in a clean, readable format
- Logs every search (city, date/time, temperature, etc.) to a local CSV file
- Handles invalid city names and failed API calls without crashing

## Tech Stack
- Python
- `requests` — for calling the weather and geocoding APIs
- `csv` — for logging search history
- [Open-Meteo](https://open-meteo.com/) — free weather and geocoding API, no API key required

## Installation
```bash
git clone https://github.com/DenoFury/weathercli
cd weather-dashboard-cli
pip install -r requirements.txt
```

## Usage
```bash
python weather.py
```
Enter a city name when prompted. The current weather will be displayed in the terminal and appended to `weather_history.csv`.

## Example Output
Enter city: Malaga
Weather in Malaga: 27°C, Clear sky
Logged to weather_history.csv


## Future Improvements
- Support checking multiple cities in a single run
- Add more weather details (humidity, wind speed, forecast)
- Visualize logged history with a simple chart

## Lessons Learned
First project combining an external API, JSON parsing, and CSV persistence in one script. Learned to handle two-step API calls (geocoding a city name into coordinates before fetching weather data) and to build in error handling for invalid input and failed requests.