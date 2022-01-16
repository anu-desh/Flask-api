import imp
from space import app
from flask import render_template,request,redirect,flash,url_for,jsonify
from space.models import User
from space import db

@app.route('/')
def hello(name=None):
    return render_template('hello.html',name = name)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(name = request.form["name"],email = request.form["email"])
        db.session.add(user)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('users'))
    return render_template('login.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users = users)

@app.route('/json')
def json():
    users = User.query.all()
    return jsonify([user.serialize for user in users])

@app.errorhandler(404) 
def error(error):
    return render_template('notfound.html'),404