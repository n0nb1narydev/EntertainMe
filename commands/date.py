# numbersapi.com/1/25/date

import requests

def get_date_fact(month, day):
    response = requests.get(f"http://numbersapi.com/{month}/{day}/date")
    data = response.content.decode()

    return data