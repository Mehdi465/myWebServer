from flask import Flask,render_template,request
import json
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")



@app.route("/")
@app.route("/home",methods=["POST"])
def register_new_word():
    
    with open("json_file/DB.json","r+") as json_file:

        list_ = json.load(json_file)

    if len(list_) > 0:
    
        N = max([list_[x]["id"] for x in range(len(list_))])+1
    else:
        N=1

    new_word = {"id":N,"word":request.form["word"],"definition":request.form["definition"]}

    list_.append(new_word)

    with open("json_file/DB.json","w") as file:
        json.dump(list_,file)

    return render_template("home.html")
    


@app.route("/exam",methods=["GET"])
def exam_page():

    with open("json_file/DB.json","r+") as json_file:
        dict_ = json.load(json_file)
   
    return render_template("exam.html",items=dict_)







