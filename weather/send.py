import requests


def send(key, host, country):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"  # open weather url endpoint
    querystring = {"q": country, "units": "metric"}  # my query
    headers = {
        'x-rapidapi-host': host,
        'x-rapidapi-key': key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    return response
