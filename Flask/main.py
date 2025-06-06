from flask import Flask
from flask import render_template
from flask import request

app = Flask("app")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['fname']
    return f'Hello, {name}'
    
app.run(debug=True)