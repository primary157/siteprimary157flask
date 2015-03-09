from flask import render_template
from app import app
from flask import request
import getpass


@app.route('/')
@app.route('/index')
def index():
    info = request.headers.get('User-Agent')
    infos = info.replace(')', ' ').replace('(', ' ').split(' ')
    OS = infos[1] + ' ' + infos[2] + ' ' + infos[3] + ' ' + infos[4]
    OS = OS.replace(';', '')
    username = getpass.getuser()
    if 'chrome' in info or 'Chrome' in info:
        browser = 'Chrome'
    elif 'Opera' in info or 'opera' in info:
        browser = 'Opera'
    elif 'Safari' in info or 'safari' in info:
        browser = 'Safari'
    elif 'Firefox' in info or 'firefox' in info:
        browser = 'Firefox'
    else:
        browser = 'Unknown browser'
    user = {
            'nickname': username,
            'browser': browser,
            'OS': OS,
           }  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
