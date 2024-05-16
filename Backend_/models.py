#database models and how we interact with it. the sqlalchemy creates a python classs that we can define like a table we can store
#imports db from config file
from config import db

#This is a database model represented as a python class. Using code we will set up fiels

class Contact(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        #you have to pass string limit. cant pass null value for name
        #this are different fields being stored in Contact. We will convert them using JSON and pass to front end
        first_name = db.Column(db.String(80), unique=False, nullable=False)
        last_name = db.Column(db.String(80), unique=False, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        
        #takes the different fields converts into a Python dictionary which converts to JSON that we can pass from API. This JSON
        #is how we communicate with the api
        #camelcase for JSON
        def to_json(self):
                return {
                        "id": self.id,
                        "firstName": self.first_name,
                        "lastName": self.last_name,
                        "email": self.email,
                }