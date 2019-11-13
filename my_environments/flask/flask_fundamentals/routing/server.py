from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/', methods = 'POST')          # The "@" decorator associates this route with the function immediately following
def index():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def heloo_dojo():
    return 'Dojo'


# have it say "Hi Flask!"

@app.route('/say/<name>')     
def say_name(name):
    return 'hello '+ name

# /repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<num>/<word>')
def repeat_word(num,word):
   
    return word* int(num)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 