import requests


def get_api_url(api_key, **kwargs):
    API_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    for query, value in kwargs.items():
        API_URL += f'{query}={value}&'

    API_URL += f'appid={api_key}'
    return API_URL


def get_weather(api_key: str, location: str, **kwargs):
    response = requests.get(get_api_url(api_key, q=location)).json()
    return response





