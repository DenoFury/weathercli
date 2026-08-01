import requests
city = input("Which city do you live in? ")

r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json')
geocode = r.json()  # The result of city search 



params = {
  "latitude": geocode["results"][0]["latitude"],
  "longitude": geocode["results"][0]["longitude"],
  "hourly": ["temperature_2m", "weather_code"],
	"forecast_days": 3,
}

r2 = requests.get('https://api.open-meteo.com/v1/forecast', params=params)

temp = r2.json()
temperatures = {}
for date,degree,weather  in zip(temp["hourly"]["time"], temp["hourly"]["temperature_2m"], temp["hourly"]["weather_code"]):
  day = date.split("T")[0]
  if(temperatures.get(day)):
    degrees,weather_code = temperatures.get(day)
    degrees.append(degree)
    weather_code.append(weather)
    
  else:
    degrees = [degree]
    weather_codes = [weather]
    temperatures.update({day: {degrees, weather_codes}})



for days in temperatures.keys():
  print(f"Day {days}: Max: {max(temperatures.get(days))} ºC, Min: {min(temperatures.get(days))} ºC.")