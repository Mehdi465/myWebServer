from flask import Flask,render_template,request
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


""" 

@app.route("/exam")
def exam():
    with open("json_file/DB.json","r+") as json_file:
        dict_ = json.load(json_file)
        
    return render_template("transaction.html",entries=list(dict_.keys()))

 """



