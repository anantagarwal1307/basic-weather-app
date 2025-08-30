#Basic Weather App

print("BASIC WEATHER APP\n")

import requests #For generate a weather report

api_key = 'f95ada39852d103c043495713fc0cfed' #to connect the weather report

city = input("Enter city:- ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
	print("No City Found")

else:
	
	weather = weather_data.json()['weather'][0]['main']
	
	temp = round(weather_data.json()['main']['temp'])
	
	print(f"The weather in {city} is:- {weather}")
	
	print(f"The temperature in {city} is:- {temp}°C")