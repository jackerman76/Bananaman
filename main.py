import datetime
from flask import Flask, request, redirect, render_template, url_for, jsonify, session
from user import *
from data_access import *
from post import *
from request import *
#import fileapp
import urllib
from uploadedFile import UploadedFile
from displayInfo import DisplayInfo
from google.cloud import storage
import time
import requests
import json
from utils import *

app = Flask(__name__, static_folder='static-files-folder')

app.secret_key = 'SECRET_KEY'
_BUCKET_NAME = "banana-post-pictures"

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    return (render_template("home.html"))

def about():
    return (render_template("about.html"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.form.get("create_account") == "True":
        return (redirect("create_account"))
    if request.form.get("login") == "True":
        username = request.values.get('username')
        password = request.values.get('password')
        # create user object
        user = User(username, password)
        # check if user exists
        entity = get_user_entity(user)
        if entity:
            #User exists
            user2 = entity_to_user(entity)
            if user2.password == password:
                session['username'] = username
                return (redirect(url_for('home')))
            else:
                # Username and Password do not match
                return (redirect("login"))
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
                    return(render_template("login.html"))
                else:
                    entity = user_to_entity(user)
                    update_entity(entity)
                    session['username'] = username
                    return (redirect("/"))
            else:
                #Password is not equal message
                return (render_template("create_account.html"))
    return (render_template("create_account.html"))

@app.route('/got_bananas', methods=["GET", "POST"])
def got_bananas():
    #Write post to datastore
    if not session.get('username'):
        return (redirect(url_for('login')))

    if request.method == 'POST':
        if request.form.get("request_bananas") == "True":
            quantity = request.values.get('quantity')
            description = request.values.get('description')
            username = session['username']
            # geolocation = request.values.get("geolocation")

            # location input using google maps api
            latitude = float(request.values.get("loc_lat"))
            longitude = float(request.values.get("loc_long"))
            geolocation = str([latitude,longitude])

            # availability funcitonality
            availability_start = request.values.get("availability_start")
            availability_end = request.values.get("availability_end")
            #start_timestamp = None
            #end_timestamp = None
            # chek if user provided these values
            #if availability_start and availability_end:
                #start_timestamp = datetime_input_to_timestamp(availability_start)
                #end_timestamp = datetime_input_to_timestamp(availability_end)


            # file handling
            uploaded_file = request.files['file']
            #filename = request.form.get('filename')
            file_name = uploaded_file.filename or "image_upload"
            file_name += session["username"] + str(time.time())
            gcs_client = storage.Client()
            storage_bucket = gcs_client.get_bucket(_BUCKET_NAME)
            blob = storage_bucket.blob(file_name)
            c_type = uploaded_file.content_type
            blob.upload_from_string(uploaded_file.read(), content_type=c_type)

            #fileapp.save_file(filename, blob.public_url)
            url = blob.public_url



            post = Post(username=username,
                        description=description,
                        geolocation=geolocation,
                        quantity=quantity,
                        picture=url,
                        availability_start=availability_start,
                        availability_end=availability_end,
                        status="available")
            entity = post_to_entity(post)
            update_entity(entity)
            return (redirect("/"))

    return (render_template("got_bananas.html"))

@app.route('/need_bananas', methods=["GET", "POST"])
def need_bananas():
    if request.method == 'POST':
        if request.form.get("submit_form") == "True":
            latitude = float(request.values.get("loc_lat"))
            longitude = float(request.values.get("loc_long"))
            session["latitude"] = latitude
            session["longitude"] = longitude
            radius = request.values.get("radius_input")

            if not radius:
                list = query_posts_by_location(latitude, longitude)

            else:
                radius = float(radius)
                list = query_posts_by_location(latitude, longitude, radius)

    elif session.get("latitude") and session.get("longitude"):
        list = query_posts_by_location(session["latitude"], session["longitude"])

    else: list = query_posts()

    return (render_template("need_bananas.html", list=list))

@app.route('/view_map', methods=["GET", "POST"])
def view_map():
    list = query_posts()
    return (render_template("view_map.html", list=list))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', default=None)
    return (redirect(url_for('login')))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
