from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
 
 #connecting to the database
locl_server=True
app=Flask(__name__,template_folder='templates')
app.secret_key='test'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:@localhost/gymdb'
db=SQLAlchemy(app)

@app.route('/')
def Home_page():
    return render_template('index.html')




app.run(debug=True)