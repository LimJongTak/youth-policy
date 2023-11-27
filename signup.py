from flask import render_template, request, redirect, url_for
from app import app

users = {'admin': 'admin123'}
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return render_template('signup.html', error='Username already exists')

    return render_template('signup.html', error=None)
