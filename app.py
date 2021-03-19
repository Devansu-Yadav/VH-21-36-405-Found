from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import json
from datetime import datetime

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def library():
    print("Helo")
    if request.method == 'POST':
        print("Helo")
        '''Add entry to the database'''

    return render_template('index.html')
