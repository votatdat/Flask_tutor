from flask import Flask, render_template, url_for


app = Flask(__name__)


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
def hello_world():
    return render_template('home.html', posts=posts, title=title)


@app.route('/about')
def about():
    return render_template('about.html')
