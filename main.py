from flask import Flask,render_template,request,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,LoginManager,login_manager
from flask_login import login_required, current_user
 
#connecting to database
locl_server=True
app=Flask(__name__, template_folder='templates',static_folder='static')

app.secret_key='test'

login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

@app.route('/member')
def member():
    return render_template('member_area.html')



@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('member'))
        else:
            print("invalid credentials")
            return render_template("mem_login.html")
    
    return render_template('mem_login.html')

@app.route('/signup',methods=['post','get'])
def signup():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            print("email already exists")
            return render_template('mem_signup.html')
        
        encpassword=generate_password_hash(password)

        #new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES('{username}','{email}','{encpassword}')")
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        return render_template('mem_login.html')
        
    

    return render_template('mem_signup.html')




  
 

app.run(debug=True)