import os

from flask import Flask, render_template, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

posts = [
    {
        'author': 'Dat Vo',
        'title': 'First blog',
        'content': 'This is the first blog.',
        'date_posted': '2020, Aug, 13'
    },
    {
        'author': 'Thien Pham',
        'title': 'Second blog',
        'content': 'This is the second blog.',
        'date_posted': '2021, Jan, 15'
    }
]

title = "Dat"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title=title)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)