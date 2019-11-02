from flask import Flask ,render_template 
app = Flask(__name__)  

@app.route('/play')          
def hello_world():
    return render_template('index.html',   new_play= 3,color="blue" )

@app.route('/play/<x>')
def many_boxes(x):
    return render_template('index.html', new_play = int(x), color="blue" )

@app.route('/play/<x>/<color>')
def colors(x, color):
    return render_template('index.html',  new_play = int(x), color=color)

if __name__=="__main__":      
    app.run(debug=True)