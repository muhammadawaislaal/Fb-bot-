import requests
import random

def get_free_proxy():
    url = "https://www.proxy-list.download/api/v1/?type=http"
    response = requests.get(url).text.splitlines()
    if response:
        return random.choice(response)
    return None