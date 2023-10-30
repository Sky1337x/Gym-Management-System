from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def Home_page():
    return render_template('index.html')

app.run(debug=True)