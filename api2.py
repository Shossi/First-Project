import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--city', action='store', dest='city', help='usage : -c "New York"', required=True)
result = parser.parse_args()
# city = input('Please input your chosen city: ')
url = 'https://community-open-weather-map.p.rapidapi.com/forecast/daily'

querystring = {"q": result.city, "units": "metric"}
# result.city
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "6c6a60cc8fmsh9b946eda4e995e1p18a674jsn70a66ab4190b"
}

response = requests.request("GET", url, headers=headers, params=querystring)
try:
    # print(response.text)
    response = response.json()
    country = response['city']['country']
    city = response['city']
    day = response['list'][0]['temp']['day']
    night = response['list'][0]['temp']['night']
    weather = response['list'][0]['weather'][0]['description']
    print(city, "s weather today\ntoday's temp:", day, "\ntonight's temp:", night, '\nweather:', weather)
except Exception as ex:
    print(ex)
    print('Given city does not exist')
