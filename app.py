#flask run    :::   python -m flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/felix")
def vanfelix():
    getal = 4
    resultaat = 3* getal
    return str(resultaat)

@app.route("/felix2/<voornaam>")
def vanfelix2(voornaam):
    getal = 4
    resultaat = 3* getal
    return "hoi,, "+voornaam