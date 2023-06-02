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
weather_main = weather_data['weather'][0]['main']

# README用の文字列を構築
readme_text = f"temperature: {temperature}℃\n\n\nhumidity: {humidity}%\n\n\nweather:{weather_main}"

# READMEファイルを更新
with open('README.md', 'r') as f:
    content = f.read()
    new_content = content.replace('WEATHER_INFORMATION',readme_text)
    if weather_main == 'Clear':
        new_content = new_content.replace('IMAGE_URL_DAY',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/d53eec19-1fa1-4aaa-8752-56c1bb7ba273")
        new_content = new_content.replace('IMAGE_URL_NIGHT',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/da49294a-3706-4daf-8bf9-f8ab99fcb824")
    elif weather_main == 'Clouds':
        new_content = new_content.replace('IMAGE_URL_DAY',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/d53eec19-1fa1-4aaa-8752-56c1bb7ba273")
        new_content = new_content.replace('IMAGE_URL_NIGHT',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/8b5437f7-9550-4388-9d13-1765240d709d")
    elif weather_main == 'Rain':
        new_content = new_content.replace('IMAGE_URL_DAY',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/532b7cb3-374f-4b90-aa2e-5c322a6cdd9c")
        new_content = new_content.replace('IMAGE_URL_NIGHT',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/88d46e58-a771-48fc-b1e3-aa80add5833c")
    elif weather_main == 'Snow':
        new_content = new_content.replace('IMAGE_URL_DAY',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/d9038324-0e4e-41c8-9b97-1ae153da8b55")
        new_content = new_content.replace('IMAGE_URL_NIGHT',"https://github.com/Yamayamaaya/Yamayamaaya/assets/100800509/d1e3d163-212a-4c12-8a41-c114713a6373")
        
        
with open('README.md', 'w') as f:
    f.write(new_content)
