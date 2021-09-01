import os

from flask import Flask, render_template, flash, redirect, url_for, request ,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from sqlalchemy.sql.elements import Null


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/github_users.db'
app.config['SECRET_KEY'] = 'Ike-ximenez2021'

db = SQLAlchemy(app) 

# GITHUB_USERS class for SQLAlchemy

class GITHUB_USERS(db.Model):
 ID = db.Column(db.Integer, primary_key=True)
 ID_USER = db.Column(db.Integer)
 USER_NAME = db.Column(db.String(50))
 AVATAR = db.Column(db.String(250))
 USER_TYPE = db.Column(db.String(50))
 URL = db.Column(db.String(250))
 
 # Class for the Marshmellow Schema 
class UserSchema(Schema):
    ID = fields.Integer()
    ID_USER = fields.Integer()
    USER_NAME = fields.Str()
    AVATAR = fields.Str()
    USER_TYPE = fields.Str()
    URL = fields.Str()

# Routes for pagination management 
@app.route("/")
@app.route("/users")
@app.route("/users/<int:page_num>")
def users(page_num=None):
   users_ppage=request.args.get('pagination',default=25,type=int) 
   users = GITHUB_USERS.query.paginate(per_page=users_ppage, page=page_num, error_out=True)
   return render_template('index.html', users=users  )

# Routes for GET API REST Endpoint based on pagination request
@app.route("/api/users/profiles", methods=['GET'])
def profiles():    
   users_ppage=request.args.get('pagination',default=25,type=int) 
   page_num=request.args.get('page',default=1,type=int)
   user_name=request.args.get('username',default="",type=str)
   id_user=request.args.get('id',default=0,type=int)
   user_order_by = request.args.get('order_by',default="",type=str)

   user_schema = UserSchema() 
   users = GITHUB_USERS.query.paginate(per_page=users_ppage, page=page_num, error_out=True)
   json_string = user_schema.dumps(users.items, many=True)

   if user_name != "" :
      q_user_name = db.session.query(GITHUB_USERS).filter_by(USER_NAME=user_name)
      json_string = user_schema.dumps(q_user_name, many=True)

   if id_user > 0 :
       q_id_user = db.session.query(GITHUB_USERS).filter_by(ID_USER=id_user)
       json_string = user_schema.dumps(q_id_user, many=True)

   if user_order_by != "" :
      if user_order_by == "id" :
         user_order_by = "ID_USER"
      if user_order_by == "type" :
         user_order_by = "USER_TYPE"
      q_order_by = db.session.query(GITHUB_USERS).order_by(user_order_by).limit(100)
      json_string = user_schema.dumps(q_order_by, many=True)
   
   return json_string



if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(debug=True,host='0.0.0.0', port=port)

