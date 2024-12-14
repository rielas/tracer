import requests
import time
import random

while True:
    try:
        response = requests.get('http://web-server:5000')
        print(f"Request sent, received status code: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")

    time.sleep(random.uniform(1, 5))
