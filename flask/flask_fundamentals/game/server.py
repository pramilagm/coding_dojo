from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>welcome to the Park where do you wanna go left or right </h1>'


@app.route('/left')
def left_way():
    return '<h3>welcome too the zoo what do you  wanna see TIGER or MONKEY</3>'

@app.route('/left/tiger')
def tiger():
    return '<h3>the tiger is very angry Be careful'

@app.route('/left/monkey')
def monkey():
    return '<h3>the monkey is very hungry give him a Bannana'

@app.route('/right')
def right_way():
    return "ohhh no you are in the Hell Dont be afraid thers a some way you can ouf of here if you choose the right way chose the no between 1 to 5  "

@app.route('/right/<select_num>')

def choose_num(select_num):
    num = int(select_num)
    if num<=+2:
        return 'Unfortunely you ll be killed'
    elif num ==3 or num ==4:
        return 'you still have some chance to escape'
    else:
        return 'You are lucky u are out of the hell'


if __name__ =='__main__':
    app.run(debug = True)



