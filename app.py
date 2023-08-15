from flask import Flask,render_template,request
import json


app = Flask(__name__)




# ------------------- Home part -------------------
@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def menu_site():
    if request.method == "POST":
        if request.form.get("1") == "BeAGenius":
            return render_template("beagenius_home.html")

    else:
        return render_template("Home_menu.html")








# ------------------- BeAGenius part -------------------

@app.route("/beagenius/")
@app.route("/beagenius/home")
def home_page():
    return render_template("beagenius_home.html")



#Cope only with POST requests in the home page.
@app.route("/beagenius")
@app.route("/beagenius/home",methods=["POST"])
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

    return render_template("beagenius_home.html")
    

# Cope with the exam page, only GET requests
@app.route("/beagenius/exam",methods=["GET"])
def exam_page():

    with open("json_file/DB.json","r+") as json_file:
        dict_ = json.load(json_file)
   
    return render_template("beagenius_exam.html",items=dict_)







