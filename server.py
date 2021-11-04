from flask import Flask, render_template, redirect, request
from model_users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())


@app.route('/users/new')
def new_form():
    return render_template("add_new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form) 
    return redirect('/users')




if __name__ == "__main__":
    app.run(debug = True)
