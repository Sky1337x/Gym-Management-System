from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
 
#connecting to database
locl_server=True
app=Flask(__name__, template_folder='templates',static_folder='static')

app.secret_key='test'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/gymdb'
db=SQLAlchemy(app)

#this is the landing page
@app.route('/')
def Home_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


  
 

app.run(debug=True)