from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def hello_world():
    user = {"username": "Arkady"}
    books = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', user=user, books=books)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)