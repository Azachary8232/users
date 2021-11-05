from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User


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
    id = User.create(request.form)
    print(id)
    return redirect(f'/user/{id}')

@app.route('/user/<int:id>')
def show_user(id):
    data = {"id":id}
    return render_template('user.html', user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def user_edit(id):
    data= {'id':id}
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/edit', methods=['POST'])
def edit():
    User.edit(request.form)
    id = request.form.get('id')
    return redirect(f'/user/{id}')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {'id':id}
    User.delete(data)
    return redirect('/users')

