import datetime
from flask import Flask, request, redirect, render_template, url_for, jsonify, session
from user import *
from data_access import *
from post import *
from request import *

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return (render_template("home.html"))

def about():
    return (render_template("about.html"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.form.get("create_account") == "True":
        return (render_template("create_account.html"))
    if request.form.get("login") == "True":
        username = request.values.get('username')
        password = request.values.get('password')
        # create user object
        user = User(username, password)
        # check if user exists
        entity = get_user_entity(user)
        user2 = entity_to_user(entity)
        if username == user2.username and password == user2.password:
            return (render_template("home.html"))
        else:
            # Username or Password does not exist
            return (redirect("login"))

    #return render_template("home.html")
    return (render_template("login.html"))

@app.route('/create_account', methods=["GET", "POST"])
def create_account():
    if request.method == 'POST':
        if request.form.get("create_account") == "True":
            email = request.values.get('email')
            username = request.values.get('username')
            password1 = request.values.get('password')
            password2 = request.values.get('password2')
            if password1 == password2:
                # account can be successfully created
                # create user object
                user = User(username, password1, email)

                temp = get_user_entity(user)
                if temp:
                    #User already exists error
                    entity_to_user(temp)
                    return(render_template("create_account.html"))
                else:
                    entity = user_to_entity(user)
                    update_entity(entity)
                    return (redirect("home"))
            else:
                #Password is not equal message
                return (render_template("create_account.html"))
    return (render_template("create_account.html"))

@app.route('/got_bananas', methods=["GET", "POST"])
def got_bananas():
    return (render_template("got_bananas.html"))

@app.route('/need_bananas', methods=["GET", "POST"])
def need_bananas():
    if request.method == 'POST':
        if request.form.get("request_bananas") == "True":
            return (render_template("need_bananas.html"))
    return (render_template("need_bananas_form.html"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
