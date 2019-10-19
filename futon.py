# 引数に都市名の入力が必要
import requests
import json
import sys

# OpenWeatherMap
def get_weather(credentials):
    api = "http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={key}"
    city_name = "Kawasaki"
    url = api.format(city=city_name, key=credentials)
    print(url)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    return(data)


# GoogleCalendar
def post_webhook():
    api = "https://maker.ifttt.com/trigger/{event}/with/key/{key}"
    url = api.format(event="weekend_sunny", key="cNCQwgK2g30CodreX-Ensh")
    response = requests.post(url)
    # data = json.loads(response.text)
    # print(data)
    # return(data)


# pubsub
def hello_pubsub(event, context):
    W_API_KEY = "3ef6234a0f6245e278f1fbef05b06657"
    data = get_weather(W_API_KEY)

    weather = data['list'][3]['weather'][0]['main']
    
    print("天気：" + weather)

    if(weather == "Clear"):
        post_webhook()

    print('ok')
