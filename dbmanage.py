from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/github_users.db"
db = SQLAlchemy(app)
migrate=Migrate(app,db) #Initializing migrate.
manager = Manager(app)
manager.add_command('db',MigrateCommand)
 
# GITHUB_USERS class for SQLAlchemy

class GITHUB_USERS(db.Model):
 ID = db.Column(db.Integer, primary_key=True)
 ID_USER = db.Column(db.Integer)
 USER_NAME = db.Column(db.String(50))
 AVATAR = db.Column(db.String(250))
 USER_TYPE = db.Column(db.String(50))
 URL = db.Column(db.String(250))
 

if __name__ == "__main__":
      manager.run()