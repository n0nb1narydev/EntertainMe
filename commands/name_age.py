# https://api.agify.io/?name=

import requests

def get_name_age(choice):
    response = requests.get(f"https://api.agify.io/?name={choice}")
    data = response.json()
    name_age = data['age']

    return name_age