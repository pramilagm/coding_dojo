from flask import Flask,session,render_template,redirect,request
import random
app = Flask(__name__)
app.secret_key ="hello"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if 'gold' not in session:
        session['gold']= 0
        session['activities'] = []
    return render_template('index.html', gold_earned = session['gold'], log =session['activities'])

@app.route('/process_money',methods =['POST'])
def processs_money():
    if request.form['building']=="farm":
        val = random.randint(10,20)
        session['gold'] += val
        log = 'Earned' + str(val) + ' gold from the farm!'
        session['activities'].append(log)

    elif request.form['building']=="cave":
        val = random.randint(5,10)
        session['gold'] += val
        log = 'Earned' + str(val) + "gold from the cave"
        session['activities'].append(log)

    elif request.form['building']=="house":
        val = random.randint(2,5)
        session['gold'] += val 
        log = 'Earned' + str(val) + "gold from the house"
        session['activities'].append(log)

    elif request.form['building']=="casino":
        val = random.randint(0,50)
        session['gold'] -= val
        log = 'Enter a casino and lost' +str(val) + "gold...ouch"
        session['activities'].append(log)
    print(session['activities'])
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold'] = 0
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  