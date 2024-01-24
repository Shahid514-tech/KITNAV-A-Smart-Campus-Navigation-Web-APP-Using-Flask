from app import app
from flask_mail import Mail
import urllib
import os

# secret key for user session
app.secret_key = "ITSASECRET"

# Configure the mail server settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'shahidshaikh9936@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = 'Avengers45#'  # Your Gmail password

mail = Mail(app)

#database connection parameters
connection_params = {
    'user': 'Shahid9936',
    'password': 'wKAb3uj4JuuMBUSA',
    'host': 'ac-ie3wryh-shard-00-02.yuvdmwm.mongodb.net:27017',
    'port': 'port',
    'namespace': 'total_records',
}

# configuration.py

option_params = {
    'username': 'your_username',
    'password': 'your_password',
    'cluster': 'your_cluster',
    'database': 'your_database'
}

