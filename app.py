from tokenize import Name
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/next')
def next():
    return "Next page!"

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return "POST method!"
    else:
        return "GET method!"
@app.route('/hello')
def hello(name="Max"):
    return render_template('hello.html',name = name)

@app.errorhandler(404) 
def error(error):
    return render_template('notfound.html'),404

if __name__ == "__main__":
    app.run(debug = True)