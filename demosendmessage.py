import requests
TOKEN = "5711473499:AAE601T5yTeKgGWxomyyHeGXZy_33tCvypQ"
chat_id = "1318776695"
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message