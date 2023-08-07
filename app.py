from flask import Flask,render_template,request
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/exam")
def exam_page():
    return render_template("exam.html")



