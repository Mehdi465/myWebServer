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
    """ try:
        with open("json_file/DB.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
    # If the file doesn't exist yet, start with an empty list
        existing_data = []

    # Step 2: Convert the JSON data to a Python object (list of dictionaries)

    # Step 3: Append your new dictionary to the Python object
    existing_data.append(requests)

    # Step 4: Write the updated Python object back to the JSON file
    with open("json_file/DB.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4)
 """ 
    print("OOOOOOOOOOOOOOk")
    print(request.form["word"])
    return render_template("home.html")

@app.route("/exam",methods=["GET"])
def exam_page():

    with open("json_file/DB.json","r+") as json_file:
        dict_ = json.load(json_file)
   
    return render_template("exam.html",items=dict_)



