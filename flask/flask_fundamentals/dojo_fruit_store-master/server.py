from flask import Flask, render_template, request, redirect

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    order_strawberry = request.form['strawberry']
    order_raspberry =  request.form['raspberry']
    order_apple = request.form['apple']
    no_of_fruits= int(order_strawberry) + int(order_raspberry) +int(order_apple)
    return render_template("checkout.html",name_on_template = request.form['first_name'],
    last_on_template =request.form['last_name'], strawberry_on_temp = order_strawberry,
    Raspberry_on_temp =order_raspberry,apple_on_temp =order_apple ,
    id_on_template =request.form['student_id'],total_fruits = no_of_fruits)
    
@app.route('/fruits')         
def fruits():
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    