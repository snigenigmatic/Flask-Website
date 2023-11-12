import requests

# openweathermap.org API



user_input = input("enter city:")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID=8987e057165d2a4223dd4d8308a2ddb1")

if weather_data.json() ['cod'] == '404':
    print("no city found")
else:
    weather = weather_data.json() ['weather'] [0] ['main']
    temp = weather_data.json() ['main'] ['temp']
    print(weather_data.json())
    
