from flask import Flask,render_template, request,redirect,session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count = session['count'])

@app.route('/add')
def add():
    session['count'] += 1
    return redirect("/")

@app.route('/reset')
def reset():
    session.pop('count',None)
    return redirect('/')


if __name__ =='__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
# #...
# @app.route('/visits-counter/')
# def visits():
#     if 'visits' in session:
#         session['visits'] = session.get('visits') + 1  # reading and updating session data
#     else:
#         session['visits'] = 1 # setting session data
#     return reder_template('index.html', count = session['visits])
 
# @app.route('/delete-visits/')
# def delete_visits():
#     session.pop('visits', None) # delete visits
#     return 'Visits deleted'
# #...