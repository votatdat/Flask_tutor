import os

from flask import Flask, render_template, url_for, redirect, flash

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash(f'You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)