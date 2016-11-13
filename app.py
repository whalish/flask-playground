from flask import Flask, render_template, request, make_response
import sqlite3
app = Flask(__name__)

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/logged/', methods = ['GET', 'POST'])
def logged():
    username = request.form['usr']
    return "Welcome, %s" % username

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
   app.run(debug = True)