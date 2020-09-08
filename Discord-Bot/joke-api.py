import requests

URL = 'https://official-joke-api.appspot.com/random_joke'


def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_joke():
    request = requests.get(URL)
    data = check_valid_status_code(request)

    return data
