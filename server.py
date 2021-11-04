from flask import Flask, render_template, redirect, request
from model_users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())


@app.route('/users/create_user')
def new_form():
    return render_template("add_new_user.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form) 
    User.create(request.form)
    return redirect('/users')

@app.route('/user/<int:id>')
def show_user(id):
    data = {"id":id}
    print(data)
    return render_template('user.html', user=User.get_one(data))




if __name__ == "__main__":
    app.run(debug = True)
