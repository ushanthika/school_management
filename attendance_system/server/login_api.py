from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY']='265989ce38db4ace9c3415ac6e57e6ef'



@app.route('/')
def home():
   if not session.get('logged_in'):
       return render_template('login.html')
   else:
       return "Logged in currently!"
       


if __name__ == "main":
    app.run(debug = True)
