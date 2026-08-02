# Weather Dashboard CLI

A command-line tool that looks up a city, fetches a 3-day weather forecast, and logs a daily summary (max/min temperature and general conditions) to a CSV file for tracking over time.

## Features
- Look up any city by name — converts it to coordinates via a free geocoding API
- Fetches a 3-day hourly forecast and groups it into daily summaries
- Displays each day's max temperature, min temperature, and a human-readable weather description (e.g. "Overcast", "Clear sky")
- Logs every lookup to `weatherLog.csv`, creating the file with proper headers on first run
- Handles invalid city names, failed requests, and unexpected API responses without crashing

## Tech Stack
- Python
- `requests` — API calls
- `csv` — persistent logging
- `os` — checking for existing log file
- [Open-Meteo](https://open-meteo.com/) — free weather + geocoding API, no API key required

## Installation
```bash
git clone https://github.com/DenoFury/weather-dashboard-cli.git
cd weather-dashboard-cli
pip install requests
python weather.py
```

## Usage
Run the script and enter a city name when prompted:
```
Which city do you live in? Malaga
Day 2026-08-02: Max: 37.2 ºC, Min: 24.3 ºC. Weather code: Clear sky
Day 2026-08-03: Max: 36.6 ºC, Min: 25.9 ºC. Weather code: Overcast
Day 2026-08-04: Max: 37.7 ºC, Min: 27.0 ºC. Weather code: Clear sky
```
Each run appends a new set of rows to `weatherLog.csv`.

## How It Works
1. Takes a city name and geocodes it into latitude/longitude via Open-Meteo's geocoding endpoint.
2. Requests a 3-day hourly forecast for those coordinates.
3. Groups the 72 hourly readings by day using `zip()` to pair timestamps, temperatures, and weather codes.
4. Computes each day's max/min temperature and determines the most common weather code for that day.
5. Maps the numeric WMO weather code to a readable description via a lookup dictionary.
6. Prints the summary and appends it to a CSV log.

## Future Improvements
- Support checking multiple cities in a single run
- Avoid duplicate/overlapping day entries across multiple runs on the same day
- Add more detail per day (e.g. humidity, wind speed)
- Swap the manual `most_common()` helper for `collections.Counter`

## Lessons Learned
First project combining two chained API calls, nested JSON parsing, and CSV persistence with correct header handling (only written once, checked via `os.path.exists`). Also the first project with deliberate error handling — figuring out which specific lines could realistically fail (bad city name, connection issues, malformed API responses) and wrapping only those, rather than a single broad try/except around everything.