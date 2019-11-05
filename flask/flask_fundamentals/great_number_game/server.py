from flask import Flask,render_template, request,redirect,session	                # import the random module
from random import randint
app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def index():
   
     return render_template('index.html',new_num= session['number'])

@app.route('/process', methods = ['POST'])
def process_form():
    session['number'] = request.form['number']
    return redirect('/')
   


app.run(debug=True)
