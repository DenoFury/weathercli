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
git clone https://github.com/DenoFury/weather-dashboard-cli.git
cd weather-dashboard-cli
pip install -r requirements.txt
```

## Usage
```bash
python weather.py
```
Enter a city name when prompted. The current weather will be displayed in the terminal and appended to `weather_history.csv`.

## Example Output