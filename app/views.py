from flask import request, render_template, session, redirect, url_for
from .database.database_controller import Database
from app import app

db = Database('database_name')  # TODO connect to a database sure


@app.route('/')
@app.route('/home', methods=["GET"])
def home():
    if request.method == "GET":
        return render_template('home.html')
    else:
        return "neither post or get, im confused"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        if username == "" and password == "":
            return redirect(url_for('admin'))
        else:
            return "You arent an admin sorry mate"


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    pass


@app.route('/band', methods=['GET'])
def band():
    if request.method == "GET":
        return render_template('band.html')


@app.route('/gigs', methods=['GET'])
def gigs():
    if request.method == "GET":
        return render_template('gigs.html')


@app.route('/contact', methods=['GET'])
def contact():
    if request.method == "GET":
        return render_template('contact.html')
