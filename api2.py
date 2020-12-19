import json
# import ./load.py
import argparse
import send
# import requests
# global key, host


#
# def send(key, host, city):
#     url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"  # open weather url endpoint
#     querystring = {"q": city, "units": "metric"}  # my query
#     headers = {
#         'x-rapidapi-host': host,
#         'x-rapidapi-key': key
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     response = response.json()
# #   print(response)
#     city1 = response['city']['name']
#     day = response['list'][0]['temp']['day']
#     night = response['list'][0]['temp']['night']
#     weather = response['list'][0]['weather'][0]['description']
#     print("weather in", city1, "today:\nday temperature:", day, "\nnight temperature:", night, '\nweather:', weather)


def load_config():
    with open('./config.json') as json_file:
        configs = json.load(json_file)
        key = configs['config']['key']
        host = configs['config']['host']
        return key, host


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', action='store', dest='city', help='Weather and temp report of given city', required=True)
    result = parser.parse_args()
    city = result.city
    key = load_config()[0]
    host = load_config()[1]
    send.send(key, host, city)


main()
