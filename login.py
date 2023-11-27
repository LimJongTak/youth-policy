from flask import render_template, request, redirect, url_for
from app import app

users = {'admin': 'admin123'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)
