from flask import Flask, render_template

solar=Flask(__name__)

@solar.route("/")
def index():
    return render_template("SolarSystem.html")
