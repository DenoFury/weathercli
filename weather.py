import requests
import csv
import os
import sys

city = input("Which city do you live in? ")

r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json')

if(r.status_code != 200):
  sys.exit("An error ocurred (connection error/ API down)")


geocode = r.json()  # The result of city search 

if("results" not in geocode):
  sys.exit("Unexpected city given")


try:
  params = {
    "latitude": geocode["results"][0]["latitude"],
    "longitude": geocode["results"][0]["longitude"],
    "hourly": ["temperature_2m", "weather_code"],
    "forecast_days": 3,
  }
except KeyError:
  sys.exit("Unexpected result structure")

r2 = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
if(r2.status_code != 200):
   sys.exit("An error ocurred (connection error/ API down)")

temp = r2.json()
temperatures = {}
try:
  for date,degree,weather  in zip(temp["hourly"]["time"], temp["hourly"]["temperature_2m"], temp["hourly"]["weather_code"]):
    day = date.split("T")[0]
    if(temperatures.get(day)):
      degrees,weather_codes = temperatures.get(day)
      degrees.append(degree)
      weather_codes.append(weather)
      
    else:
      degrees = [degree]
      weather_codes = [weather]
      temperatures.update({day: [degrees , weather_codes]})
except KeyError:
  sys.exit("An error ocurred during data handling")


def most_common(lst):
    return max(set(lst), key=lst.count)

wmo = {
  0: "Clear sky",
  1: "Mainly clear",
  2: "Partly cloudy",
  3: "Overcast",
  45: "Fog",
  48: "Depositing rime fog",
  51: "Light drizzle",
  53: "Moderate drizzle",
  55: "Dense drizzle",
  56: "Light freezing drizzle",
  57: "Dense freezing drizzle",
  61: "Rain",
  63: "Moderate rain",
  65: "Heavy rain",
  66: "Freezing rain",
  67: "Heavy freezing rain",
  71: "Snow fall",
  73: "Moderate snow",
  75: "Heavy snow",
  77: "Snow grains",
  80: "Rain shower",
  81: "Moderate rain shower",
  82: "Heavy rain shower",
  85: "Snow shower",
  86: "Heavy snow shower",
  95: "Thunderstorm",
  96: "Thunderstorm with hail",
  99: "Thunderstorm with heavy hail"
}
csv_name = "weatherLog.csv"
if not os.path.exists(csv_name):
  with open(csv_name, "a", newline="") as log:
    writer = csv.DictWriter(log, fieldnames=["city","day", "max", "min", "weather"])
    writer.writeheader()

with open(csv_name, "a", newline="") as log:
  writer = csv.DictWriter(log, fieldnames=["city","day", "max", "min", "weather"])
  for days in temperatures.keys():
    print(f"Day {days}: Max: {max(temperatures.get(days)[0])} ºC, Min: {min(temperatures.get(days)[0])} ºC. Weather code: {wmo.get(most_common(temperatures.get(days)[1]))}")
    writer.writerow({"city": city, "day" : days, "max" : max(temperatures.get(days)[0]), "min": min(temperatures.get(days)[0]), "weather": wmo.get(most_common(temperatures.get(days)[1]))})
      




