import requests

API_KEY = "b60a26570bd8d01ab8d0c3aa9958338c"  # 🔑 API Key kamu
CITY = "Jakarta"  # kamu bisa ubah ke kota kamu
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=id"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        if data["cod"] != 200:
            return "Maaf, saya tidak bisa mengambil data cuaca sekarang."

        kondisi = data["weather"][0]["description"]
        suhu = data["main"]["temp"]
        kelembapan = data["main"]["humidity"]

        return f"Cuaca di {CITY} saat ini {kondisi}, suhu {suhu}°C, dengan kelembapan {kelembapan}%."
    except Exception as e:
        return f"Terjadi kesalahan saat mengambil data cuaca: {e}"
