from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')         
def index():
    return render_template("index.html") 

@app.route('/<x>')
def x_rows(x):
    new_x = int(x)
    return render_template("index.html", x_on_template =new_x )
@app.route('/<x>/<y>')
def y_rows(x,y):
    new_y = int(y)
    return render_template("index.html", x_on_template=new_y,  y_on_template =new_y )

if __name__=="__main__":   
    app.run(debug=True) 