from flask import Flask,render_template,request
import json

app = Flask(__name__)



@app.route("/",methods=["GET","POST"])
def home():
    dict_ = {}

    #print("origine : " + str(request.headers))

    if len(request.args) != 0:
        dict_[request.args.to_dict()["word"]]=request.args.to_dict()["value"]

    try:
        with open("json_file/DB.json", "r") as json_file:
            existing_data = json.load(json_file)

    except FileNotFoundError:
    # If the file doesn't exist yet, start with an empty list
        existing_data = []

    # Step 2: Convert the JSON data to a Python object (list of dictionaries)
    print(existing_data)
    # Step 3: Append your new dictionary to the Python object
    existing_data.update(dict_)

    # Step 4: Write the updated Python object back to the JSON file
    with open("json_file/DB.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

    return render_template("form.html")


@app.route("/exam")
def exam():
    with open("json_file/DB.json","r+") as json_file:
        dict_ = json.load(json_file)
        print(dict_)
    return render_template("transaction.html",entries=dict_)

