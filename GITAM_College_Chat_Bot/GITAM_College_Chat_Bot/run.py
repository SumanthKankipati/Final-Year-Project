import asyncio
from datetime import date
from msg_validate import chk_msg
from Database import InsertData, read_cred
from flask import Flask, request, render_template, redirect, jsonify
from Chat_Bot_Engine.prediction.predict import chatbot_response
from Chat_Bot_Scraper.scraper import get_scraper_result

app = Flask(__name__, static_url_path='/static')
today = date.today()
global resp
resp = ['there']

asyncio.set_event_loop(asyncio.new_event_loop())


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def login():
    global resp

    if request.form.get('sign_up') != None:
        return redirect("/register")

    elif request.form.get('sign_in') != None:
        email = request.form['username']
        passw = request.form['password']
        resp = read_cred(email, passw)
        if resp != None:
            return redirect("/chatBot")
        else:
            message = "Username and/or Password incorrect.\\n        Yo have not registered Yet \\nGo to Register page and do Registration";
            return "<script type='text/javascript'>alert('{}');</script>".format(message)

    elif request.form.get('guest_login') != None:
        resp = ['there']
        return redirect("/chatBot")

    return render_template('index.html')


@app.route("/chatBot", methods=["GET", "POST"])
def chatBot():
    global resp
    return render_template("/Chatbot_new_GUI.html", value=resp[0])


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
        InsertData(uname, email, passw, rollNo, year, sem, branch, today)
        return redirect("/")
        # render_template("index.html",email=email,password=passw)

    return render_template("Register_NewUser.html")


@app.route("/ask", methods=["POST"])
def chat_msg():
    global resp
    if request.method == "POST":
        message = request.form['messageText'].strip()

        bot_resp_from_validate = chk_msg(message, resp)

        if bot_resp_from_validate != None:
            return jsonify({'status': 'OK', 'answer': bot_resp_from_validate})

        else:
            chat_bot_resp = chatbot_response(message)
            if chat_bot_resp == "Search on Google":
                scraper_result = get_scraper_result(message)
                return jsonify({'status': 'OK', 'answer': scraper_result})
            else:
                return jsonify({'status': 'OK', 'answer': chat_bot_resp})



@app.route("/time_table")
def time_table():
    sem = request.args['sem']
    return render_template('time_table.html', sem=sem)


print(chatbot_response("Good to see you"))
if __name__ == '__main__':
    app.run(debug=True)
