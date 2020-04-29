from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/Map")
def Map():
    return render_template("map.html")

@app.route("/Offenses")
def Offenses():
    return render_template("Offenses.html")



@app.route("/premises")
def premises():
    return render_template("premises.html")