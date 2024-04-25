
from flask import Flask, render_template, request

app = Flask(__name__)
login = {}
@app.route("/", methods=["POST","GET"])
def hello_world():

        
    if request.method == "GET":

        return render_template("index.html")

    else:
        user = request.form["un"]
        password = request.form["pw"]
        print(user)

        if user in login:
            if login[user]['password'] == password:
                return "Hello " + user
            else:
                return "Invalid Password"

        else:
            return "Invalid Username"

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        user = request.form["un"]
        password = request.form["pw"]
        login[user]['username'] = user
        login[user]['password'] = password
        return render_template("index.html")

 

app.run(host="0.0.0.0",debug=True)
