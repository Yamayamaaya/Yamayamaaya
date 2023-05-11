import os
import requests

# OpenWeather APIのエンドポイントURL
url = f"http://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid={os.environ['OPENWEATHER_API_KEY']}&units=metric"

# APIにリクエストを送信して天気情報を取得
response = requests.get(url)
weather_data = response.json()

# 取得した天気情報から必要な情報を抽出
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
weather_description = weather_data['weather'][0]['description']

# README用の文字列を構築
readme_text = f"現在の天気: {weather_description}\n温度: {temperature}℃\n湿度: {humidity}%"

# READMEファイルを更新
with open('README.md', 'r+') as f:
    content = f.read()
    new_content = content.replace('OLD_STRING',readme_text)
    f.write(new_content)
