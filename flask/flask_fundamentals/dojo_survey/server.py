from flask import Flask,render_template,request,redirect  
app = Flask(__name__)
@app.route('/')  
def users():
    return render_template('index.html')  

@app.route('/process', methods =['POST'])          
def processs():
    print(request.form)
    name_from_form = request.form['name']
    city_from_form = request.form['cities']
    selected = request.form.getlist('hobies')
   

  

    return render_template('info.html', name_on_template =name_from_form, city_on_template =city_from_form, 
    language_on_template =request.form['Language'],hobies_on_template = selected, comments = request.form['folks_comments'])

if __name__=="__main__":   
    app.run(debug=True) 