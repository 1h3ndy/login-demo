
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hello_world():

        
    if request.method == "GET":

        return render_template("index.html")

    else:
        user = request.form["un"]
        password = request.form["pw"]
        print(user)
        if user == "admin" and password == "monkeys":
            return "Hello Admin"
        else:
            return "Hello " + user
        



app.run(host="0.0.0.0",debug=True)
