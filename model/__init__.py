from app import app
from flask import request, session
from helpers.database import db  # Change the database reference
from helpers.hashpass import getHashed
from helpers.mailer import sendmail
from bson import json_util, ObjectId
import json
from pymongo import MongoClient


# Assuming you have initialized 'db' database reference

def checkloginusername():
    username = request.form["username"]
    check = db.users.find_one({"username": username})  # Change the collection reference
    if check is None:
        return "No User"
    else:
        return "User exists"

def checkloginpassword():
    username = request.form["username"]
    check = db.users.find_one({"username": username})  # Change the collection reference
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == check["password"]:
        sendmail(subject="Login on Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=check["email"], body="You successfully logged in on Flask Admin Boilerplate")
        session["username"] = username
        return "correct"
    else:
        return "wrong"

def checkusername():
    username = request.form["username"]
    check = db.users.find_one({"username": username})  # Change the collection reference
    if check is None:
        return "Available"
    else:
        return "Username taken"

def registerUser():
    fields = [k for k in request.form]                                      
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user_data = json.loads(json_util.dumps(data))
    user_data["password"] = getHashed(user_data["password"])
    user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    

    # Assuming 'users' is the collection name within the 'db' database
    db.users.insert_one(user_data)  # Change the collection reference

    client = MongoClient('mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/')
    database = client[data["username"]]
    options_collection = database['options']
    
    sendmail(subject="Registration for Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=user_data["email"], body="You successfully registered on Flask Admin Boilerplate")
    print("Done")
    return user_data["password"]

