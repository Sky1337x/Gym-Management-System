from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,LoginManager,login_manager
 
#connecting to database
locl_server=True
app=Flask(__name__, template_folder='templates',static_folder='static')

app.secret_key='test'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/gymdb'
db=SQLAlchemy(app)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))


#this is the landing page
@app.route('/')
def Home_page():

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup',methods=['post','get'])
def signup():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            print("email already exists")
            return render_template('/signup.html')
        
        encpassword=generate_password_hash(password)

        #new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES('{username}','{email}','{encpassword}')")
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        return render_template('login.html')
    

    return render_template('signup.html')


  
 

app.run(debug=True)