import requests


def get_api_url(api_key, **kwargs):
    API_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    for query, value in kwargs.items():
        API_URL += f'{query}={value}&'

    API_URL += f'appid={api_key}'
    return API_URL


def get_weather(location: str, api_key: str, **kwargs):
    response = requests.get(get_api_url(api_key, q=location)).json()
    return response




# print(get_api_url('131', lat=12, lon=13))
print(get_weather('London', 'd3f243d96fd958c518995fa949ee0a9a'))



