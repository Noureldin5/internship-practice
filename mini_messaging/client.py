import requests

BASE_URL = "http://127.0.0.1:8000"

def send(user, text):
    r = requests.post(f"{BASE_URL}/send/", json={"user": user, "text": text})
    print(r.json())

def get_messages():
    r = requests.get(f"{BASE_URL}/messages/")
    for msg in r.json():
        print(f"{msg['user']}: {msg['text']}")
