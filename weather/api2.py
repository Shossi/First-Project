from flask import Flask, render_template, request
import json
import send

app = Flask(__name__)


def load_config():
    with open('config.json') as json_file:
        configs = json.load(json_file)
        key = configs['config']['key']
        host = configs['config']['host']
        return key, host


@app.route('/')
def main():
    city = request.args.get("city", "")
    if city:
        weather = city_data(city)
    else:
        weather = ""
    return (
            """<form action="" method="get">
            <center>
                    <b><h2> Welcome to my Weather Application </b></h2>
                    <b>Insert city name: </b><input type="text" name="city" value=""" + city + """>
                <input type="submit" value="Check">
            </center>
            </form>"""
            + weather
    )


def city_data(country):
    key = load_config()[0]
    host = load_config()[1]
    response = send.send(key, host, country)
    city1 = response['city']['name']
    day = response['list'][0]['temp']['day']
    night = response['list'][0]['temp']['night']
    weather = response['list'][0]['weather'][0]['main']
    return '''<center>
        <b><p style="margin-right:7.25cm">City:     {}.</b></p>
        <b><p style="margin-right:6.45cm">Day temp: {}.</b></p>
        <b><p style="margin-right:6cm">Night temp:  {}.</b></p>
        <b><p style="margin-right:6.5cm">Weather:   {}.</b></p>
        </center>'''.format(city1, day, night, weather)
