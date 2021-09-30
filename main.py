import datetime
from flask import Flask, request, redirect, render_template, url_for, jsonify, session


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form.get("signup") == "True":
        return (render_template("create_account.html"))
    if request.form.get("login") == "True":
        return (render_template("login.html"))
    if request.form.get("got_bananas") == "True":
        return (render_template("got_bananas.html"))
    if request.form.get("need_bananas") == "True":
        return (render_template("need_bananas.html"))
    return (render_template("home.html"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.form.get("create_account") == "True":
        return (render_template("create_account.html"))
    if request.form.get("login") == "True":
        username = request.values.get('username')
        password = request.values.get('password')
        return (render_template("home.html"))
    #return render_template("home.html")
    return (render_template("login.html"))

@app.route('/create_account', methods=["GET", "POST"])
def create_account():
    if request.method == 'POST':
        if request.form.get("create_account") == "True":
            password1 = request.values.get('password')
            password2 = request.values.get('password2')
            if password1 == password2:
                # do stuff
                return (redirect("login"))
    return (render_template("create_account.html"))

@app.route('/got_bananas', methods=["GET", "POST"])
def got_bananas():
    return (render_template("got_bananas.html"))

@app.route('/need_bananas', methods=["GET", "POST"])
def need_bananas():
    return (render_template("need_bananas.html"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)