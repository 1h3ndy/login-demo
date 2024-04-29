
from flask import Flask, render_template, request

app = Flask(__name__)
login = {}
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    if request.method == 'POST':
        print(request)
        user = request.form.get('username')
        print(user)
        password = request.form.get('password')
        print(password)
        f = open('login.txt', 'r')
        
        for line in f.readlines():
            
            line.strip()
            file_user, file_password = line.split(':')
            if file_user == user and file_password == password:
                return 'Login successful'
            else:
                return 'Invalid usernam'
    else:
            return render_template('index.html')
    


@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        user = request.form["un"]
        password = request.form["pw"]
        f = open("login.txt", "a")
        f.write(f"\n{user}:{password}")
        f.close()
        return render_template("index.html")

 

app.run(host="0.0.0.0",debug=True)
