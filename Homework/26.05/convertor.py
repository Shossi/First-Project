from flask import Flask
from flask import request

# from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    website = '''
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome to my Flask Temperature Convertor Application</h1>
    <h2>(enter a value in Celsius, and it will be converted to Fahrenheit)</h2>
    <form action="tempConversion" method="POST">
        <input type="text" name="tempInCelsius">
        <input type="submit" value="Convert">
    </form>
</body>
</html>'''
    return website


@app.route('/tempConversion', methods=['POST'])
def my_form_post():
    celsius = request.form['tempInCelsius']
    try:
        celsius = float(celsius)

        fahrenheit = celsius * 9.0 / 5 + 32
        return str(celsius) + " Celsius equals to " + str(fahrenheit) + " fahrenheit. " + \
               "Thank you very much for you choosing my application, have an awesome day!"

    except:
        return "That is not a number, you can go back and reenter the value to be a number or you can exit now, " \
               "Thank you very much for you choosing my application, have an awesome day! "


if __name__ == '__main__':
    app.run()
