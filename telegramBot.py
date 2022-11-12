import requests
TOKEN = "5711473499:AAE601T5yTeKgGWxomyyHeGXZy_33tCvypQ"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
