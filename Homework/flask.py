from flask import Flask

app = Flask(_name_)

@app.route("/")
def index():
    return "This is Flask!"

app.run()