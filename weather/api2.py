from flask import Flask
from flask import request
import json
import send

app = Flask(__name__)


def load_config():
    with open('config.json') as json_file:
        configs = json.load(json_file)
        key = configs['config']['key']
        host = configs['config']['host']
        return key, host


@app.route('/', methods=['POST'])
def main():
    data = request.get_json() or {}
    country = data['country']
    key = load_config()[0]
    host = load_config()[1]
    response = send.send(key, host, country)
    # print(response)
    city1 = response['city']['name']
    day = response['list'][0]['temp']['day']
    night = response['list'][0]['temp']['night']
    weather = response['list'][0]['weather'][0]['main']
    # answer = ("weather in", city1, "today<br/>day temperature:", day, "<br/>night temperature:", night, '<br/>weather:', weather)
    # print (answer)
    return 'City is: {}. day temp: {}. night temp: {}. weather: {}.'.format(city1, day, night, weather)
