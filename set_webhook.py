import requests
import os

url = 'https://rustambek2003.pythonanywhere.com/webhook'

Token = os.environ["TOKEN"]

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{Token}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{Token}/GetWebhookInfo", params=payload)



print(r.json())