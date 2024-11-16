from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return("Home Page")

@app.route("/anything")
def anything():
    return render_template("index.html")

