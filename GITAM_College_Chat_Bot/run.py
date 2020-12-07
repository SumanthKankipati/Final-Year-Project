from datetime import date
from Database import InsertData, read_cred
from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__,static_url_path='/static')
today = date.today()
global resp
resp = ['You']


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def login():
    global resp
    if request.form.get('sign_up')!=None:return redirect("/register")
    elif request.form.get('sign_in')!=None:
        email = request.form['username']
        passw = request.form['password']
        resp = read_cred(email,passw)
        if resp!=None:
            return redirect("/chatBot")
        else:
            message = "Username and/or Password incorrect.\\n        Yo have not registered Yet \\nGo to Register page and do Registration";
            return "<script type='text/javascript'>alert('{}');</script>".format(message)
    return render_template('index.html')



@app.route("/chatBot", methods=["GET", "POST"])
def chatBot():
    global resp
    return render_template("/Chatbot_new_GUI.html",value=resp[0])



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['username']
        email = request.form['email']
        passw = request.form['password']
        rollNo = request.form['roll_no']
        year = request.form['stud_year']
        sem = request.form['stud_sem']
        branch = request.form['stud_branch']
        InsertData(uname,email,passw,rollNo,year,sem,branch,today)
        return redirect("/")
#            render_template("index.html",email=email,password=passw)
    return render_template("Register_NewUser.html")


if __name__ == '__main__':
    app.run(debug=True)
