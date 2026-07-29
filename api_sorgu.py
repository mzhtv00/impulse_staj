import requests

API_KEY = "e60191508b62e1b17b46a693a98a4c34"
SEHIR = "Baku"
URL = "https://api.openweathermap.org/data/2.5/weather"

parametreler = {
    "q": SEHIR,
    "appid": API_KEY,
    "units": "metric",
    "lang": "tr"
    }

response = requests.get(URL, params = parametreler)
if response.status_code == 200:
    data = response.json()
    sehir = data["name"]
    sicaklik = data["main"]["temp"]
    hissedilen = data["main"]["feels_like"]
    nem = data["main"]["humidity"]
    hava_durumu = data["weather"][0]["description"]
    print(f"{sehir} Canlı Hava Durumu")
    print(f"Sıcaklık     : {sicaklik}°C")
    print(f"Hissedilen   : {hissedilen}°C")
    print(f"Nem Oranı    : %{nem}")
    print(f"Genel Durum  : {hava_durumu.capitalize()}")
elif response.status_code == 401:
    print("API key geçersiz. Hata kodu [401]")
elif response.status_code == 404:
    print("Şehir bulunamadı. Hata kodu [404]")
else:
    print(f"İstek başarısız. Hata Kodu [{response.status_code}]")