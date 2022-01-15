from flask import Flask, render_template, url_for, request, redirect
import json
import sqlite3
from database.queries import insertData, createTable
app = Flask(__name__)


def writeData(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    db = sqlite3.connect('database/contact.db')
    cursor = db.cursor()
    cursor.execute(createTable)
    db.commit()
    cursor.execute(insertData, [email, subject, message])
    db.commit()
    db.close()


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        writeData(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong."
