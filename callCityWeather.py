import requests
from datetime import datetime

API_KEY= "3196df06bb9e5404efffe613e4b65687"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input ("Please give me a city name :")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200: 
    data = response.json()
    weather = data['weather'] [0]['description']
    print("Abohowa:",weather)
    botur_tapmatra = round(data["main"]["temp"]- 273.15, 2)
    print("Tapmatra: ",botur_tapmatra, "Degree Celc")
    batas= data["wind"]["speed"]
    print("Batase Beg: ",batas,"KM/hr")
    visibility=round(data['visibility']/1000)
    print("Deishooman durooto: ",visibility,"Km")
    Pressure = data["main"]["pressure"]
    print("Pressure: ",Pressure, "Unit")
    humidity = data["main"]["humidity"]
    print("Humidity: ",humidity, "%")

    sunon= data["sys"]["sunrise"]
    dt_object = datetime.fromtimestamp(sunon)
    print("SUN SET:", dt_object)
    
    sunoff= data["sys"]["sunset"]
    sunset= datetime.fromtimestamp(sunoff)
    print("SUN Rise: ",sunset)
    
else:    
    print("There is something wrong.")
