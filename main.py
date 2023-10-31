from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
 
#connecting to database
locl_server=True
app=Flask(__name__,template_folder='templates')
app.secret_key='test'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/gymdb'
db=SQLAlchemy(app)

#initializing table in python
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    age=db.Column(db.Integer)
    contact=db.Column(db.Integer)
    dob_year=db.Column(db.Integer)

#this is the landing page
@app.route('/')
def Home_page():
    return render_template('index.html')
  
 

app.run(debug=True)