from flask import render_template, request, redirect, url_for, session
from app import app
from model import *
from pymongo import MongoClient
import datetime


@app.route('/', methods=["GET"])
def home():
    if "username" in session:
        mongo_uri = 'mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/'
        client = MongoClient(mongo_uri)
        db = client.databasename  # Replace 'your_database' with the actual name of your database

        # Retrieve the username from the session
        username = session.get('username')

        # Query MongoDB using the username
        user_data = db.users.find_one({'username': username})

        if user_data:
            # Convert MongoDB document to a dictionary
            user_info = {
                'name': user_data['name'],
            }
        return render_template('index.html', data=user_info)
    else:
        return render_template('login.html')

# Register new user
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        registerUser()
        return redirect(url_for("login"))

#Check if email already exists in the registratiion page
@app.route('/checkusername', methods=["POST"])
def check():
    return checkusername()

# Everything Login (Routes to renderpage, check if username exist and also verifypassword through Jquery AJAX request)
@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))
            


@app.route('/checkloginusername', methods=["POST"])
def checkUserlogin():
    return checkloginusername()

@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()

#The admin logout
@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop('username', None)  # remove user session
    return redirect(url_for("home"))  # redirect to home page with message

#Forgot Password
@app.route('/forgot-password', methods=["GET"])
def forgotpassword():
    return render_template('forgot-password.html')

#404 Page
@app.route('/404', methods=["GET"])
def errorpage():
    return render_template("404.html")

#Blank Page
@app.route('/blank', methods=["GET"])
def blank():
    return render_template('blank.html')


#Cards Page
@app.route('/cards', methods=["GET"])
def cards():
    return render_template('cards.html')

#Charts Page
@app.route('/charts', methods=["GET"])
def charts():
    return render_template("charts.html")

#Tables Page
@app.route('/tables', methods=["GET"])
def tables():
    return render_template("tables.html")

#Utilities-animation
@app.route('/utilities-animation', methods=["GET"])
def utilitiesanimation():
    return render_template("utilities-animation.html")

#Utilities-border
@app.route('/utilities-border', methods=["GET"])
def utilitiesborder():
    return render_template("utilities-border.html")

#Utilities-color
@app.route('/utilities-color', methods=["GET"])
def utilitiescolor():
    return render_template("utilities-color.html")

#utilities-other
@app.route('/utilities-other', methods=["GET"])
def utilitiesother():
    return render_template("utilities-other.html")

#media 
@app.route('/media', methods=["GET"])
def media():
    return render_template("media.html")

@app.route('/submit_options', methods=['POST'])
def submit_options():
    # Check if the user is logged in
    if "username" not in session:
        return redirect(url_for("login"))
    client = MongoClient('mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/')
    # Get the current username from the session
    username = session["username"]

    # Retrieve the user_db for the logged-in user
    user_db = client[username]
    # Connect to the MongoDB database
    client = MongoClient(mongo_uri)
    db = user_db

    # Specify the collection
    options_collection = db['options']
    if request.method == 'POST':
        data = request.get_json()

        # Extract data from the JSON request
        source = data.get('source')
        destination = data.get('destination')

        # Get the current date
        current_date = datetime.date.today()

        # Get the current time
        current_time = datetime.datetime.now().time()

        # Format the output
        formatted_date = current_date.strftime("%d-%m-%Y")
        formatted_time = current_time.strftime("%H:%M:%S")

        # Store options and timestamp in MongoDB
        options_collection.insert_one({
            'source': source,
            'destination': destination,
            'date': str(formatted_date),
            'time': str(formatted_time)
        })

        return "Options submitted successfully!"

# Connection URL and database name
mongo_uri = 'mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/'


@app.route('/buttons')
def buttons():
    # Check if the user is logged in
    if "username" not in session:
        return redirect(url_for("login"))

    client = MongoClient('mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/')
    # Get the current username from the session
    username = session["username"]

    # Retrieve the user_db for the logged-in user
    user_db = client[username]
    # Connect to the MongoDB database
    client = MongoClient(mongo_uri)
    db = user_db

    # Specify the collection
    collection = db['options']

    # Fetch data from the collection
    data = collection.find({})

    # Render HTML with the fetched data
    return render_template('buttons.html', data=data)

@app.route('/profile', methods=['GET'])
def profile():
    # Check if the user is logged in
    if "username" not in session:
        return redirect(url_for("login"))

    mongo_uri = 'mongodb+srv://Shahid9936:wKAb3uj4JuuMBUSA@cluster0.yuvdmwm.mongodb.net/'
    client = MongoClient(mongo_uri)
    db = client.databasename  # Replace 'your_database' with the actual name of your database

    # Retrieve the username from the session
    username = session.get('username')

    # Query MongoDB using the username
    user_data = db.users.find_one({'username': username})

    if user_data:
        # Convert MongoDB document to a dictionary
        user_info = {
            'name': user_data['name'],
            'email': user_data['email'],
            'username': user_data['username'],
            'password': user_data['password']
            # Add other fields as needed
        }

        return render_template('profile.html', data=user_info)
    else:
        return "User not found in the database."