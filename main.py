import requests

api_key = "bce0e2291bf2c9d093476a8b3a0346f4"

city = input("Enter a city:")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
# print(weather_data.json())

if weather_data.json()["cod"] == "404":
    print("City not found")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp =weather_data.json()["main"]["temp"]
    print(f"The weather in {city} is {weather} and the temperature is {round(temp-273.15)}C")