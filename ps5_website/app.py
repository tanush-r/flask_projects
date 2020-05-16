from flask import Flask, render_template, url_for, request, session, redirect, g
import sqlite3

app = Flask(__name__)


@app.route('/')
def index_redirect():
    return redirect('/index/new_user')


@app.route('/index/<name>')
def index(name):
    if name != "new_user":
        return render_template('index.html', name=name, logged=True)
    return render_template('index.html', name="new_user", logged=False)


@app.route('/home/<name>', methods=["GET", "POST"])
def home(name):
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        password = request.form['password']
        db = get_db()
        db.execute("insert into accounts(name,age,location,password) values (? ,?, ?, ?)",
                   [name, age, location, password])
        db.commit()
    if name == "new_user":
        return render_template('home.html', name="new_user", logged=False)
    return render_template('home.html', name=name, logged=True)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signin')
def signin():
    return render_template('signin.html', check=False)


@app.route('/processed', methods=['POST'])
def processed():
    name = request.form['name']
    password = request.form['password']
    db = get_db()
    cursor = db.execute("select name,password from accounts")
    data = cursor.fetchall()

    for row in data:
        if row[0] == name and row[1] == password:
            return redirect(url_for('home', name=name, logged=True))
    return render_template('signin.html', check=True)


def connect_db():
    sql = sqlite3.connect('sqlite3/ps5.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == '__main__':
    app.run(debug=True)
