#contains main configuration of the application

from flask import Flask
#Cors is cross origin request. allows us to send a request to this backend from a different URL. by default server cant get hit by a diff URL. Our frontend and backend will be on different servers
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
#specifies location of database to get saved to
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
#doesnt track all modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#creates instance of database
db = SQLAlchemy(app)