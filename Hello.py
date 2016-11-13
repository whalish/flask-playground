from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def login():
   return render_template('login.html')

@app.route('logged')
def logged():
    username = request.form['usr']
    return "welcome %s" % username
@app.route