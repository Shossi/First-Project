import requests


def send(key, host, city):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"  # open weather url endpoint
    querystring = {"q": city, "units": "metric"}  # my query
    headers = {
        'x-rapidapi-host': host,
        'x-rapidapi-key': key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    #   print(response)
    city1 = response['city']['name']
    day = response['list'][0]['temp']['day']
    night = response['list'][0]['temp']['night']
    weather = response['list'][0]['weather'][0]['description']
    print("weather in", city1, "today:\nday temperature:", day, "\nnight temperature:", night, '\nweather:', weather)

