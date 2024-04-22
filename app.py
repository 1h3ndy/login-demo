
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    user =request.args.get("name")
    print(user)
    if user == None:
    
        return render_template("index.html")
    elif user == "admin":
        return "Hello admin"
    else: 
        return "hello " + user
app.run(host="0.0.0.0",debug=True)
