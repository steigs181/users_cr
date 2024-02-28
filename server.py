from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'blueberries12345'
from users import User

@app.route('/')
def add_user():
    return render_template('create.html')

@app.route('/add_user/update', methods=['POST'])
def add_user_info():
    User.new_user(request.form)
    return redirect ('/display_user')

@app.route('/display_all')
def display_users():
    return render_template('/read.html', users= User.get_all())

@app.route('/display_one/<int:friend_id>')
def get_one_user(friend_id):
    selected_user = User.get_one()
    return render_template('read.html', selected_user = selected_user)
if __name__ == '__main__':
    app.run(debug=True)