import requests
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number', action='store', dest='number', help='example: +972542312311', required=True)

Phone = parser.parse_args()

url = "https://veriphone.p.rapidapi.com/verify"

querystring = {"phone": Phone.number}

headers = {
    'x-rapidapi-host': "veriphone.p.rapidapi.com",
    'x-rapidapi-key': "6c6a60cc8fmsh9b946eda4e995e1p18a674jsn70a66ab4190b"
}
try:
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    # print(response.text)
    print('Given phone number: ', response["phone"])
    print('Country :', response['country'])
    print('Local number :', response['local_number'])
except Exception as ex:
    print(ex)
    print('Problem with the given phone number, ')

