from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<name>/<times>')
def hello_persons(name,times):
    return render_template('name.html',some_name = name, num_times =int(times))

@app.route('/lists')
def some_list():
    some_info =[
        {'name':'michael','age':25},
        {'name':'siris','age':27},
        {'name':'pramila','age':25}
    ]

    return render_template('list.html',random_num=[1,2,4,9], new_info = some_info)

if __name__=='__main__':
    app.run(debug=True)

