import requests

def get_activity(choice):
    response = requests.get(f"http://www.boredapi.com/api/activity?type={choice}")
    data = response.json()
    activity = data['activity'].lower()

    return activity