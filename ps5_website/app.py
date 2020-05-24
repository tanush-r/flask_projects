from flask import Flask, render_template, url_for, request, session, redirect, g
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    name = request.args.get("name")
    logged = request.args.get("logged")
    if logged == None:
        logged = False
    return render_template('index.html', name=name, logged=logged)


@app.route('/game/')
def game():
    name = request.args.get("name")
    logged = request.args.get("logged")
    type = request.args.get("type")
    db = get_db()
    cursor = db.execute("select id,name,desc,price,img_key,type from games")
    data = cursor.fetchall()
    cursor = db.execute("select id from accounts where name == ?", [name])
    acc_id = cursor.fetchone()
    cursor = db.execute("select acc_id,game_id from acc_game")
    acc_game = cursor.fetchall()
    cart_game = []
    if logged == None:
        return render_template('game.html', name=name, logged=False, games=data, type=type, cart=[])
    for g in acc_game:
        if g[0] == acc_id[0]:
            cart_game.append(g[1])
    return render_template('game.html', name=name, logged=True, games=data, acc_id=acc_id[0], type=type, cart=cart_game)


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
    cursor = db.execute("select id,name,password from accounts")
    data = cursor.fetchall()
    for row in data:
        if row[1] == name and row[2] == password:
            return redirect(url_for('game', name=name, logged=True, type="new"))
    return render_template('signin.html', check=True)


@app.route('/new', methods=['POST'])
def new():
    name = request.form['name']
    age = request.form['age']
    location = request.form['location']
    password = request.form['password']
    db = get_db()
    db.execute("insert into accounts(name,age,location,password) values (? ,?, ?, ?)",
               [name, age, location, password])
    db.commit()
    return redirect(url_for("game", name=name, logged=True, type="new"))


@app.route('/buy/')
def buy():
    name = request.args.get("name")
    acc_id = request.args.get("acc_id")
    game_id = request.args.get("game_id")
    db = get_db()
    db.execute("insert into acc_game(acc_id,game_id) values (? ,?)",
               [acc_id, game_id])
    db.commit()
    return redirect(url_for('cart', name=name))


@app.route('/delete/')
def delete():
    name = request.args.get("name")
    acc_id = request.args.get("acc_id")
    game_id = request.args.get("game_id")
    print(type(acc_id),game_id,name)
    db = get_db()
    cur = db.execute("select * from acc_game")
    i = cur.fetchall()
    db.execute("delete from acc_game where acc_id == ? and game_id == ?",[acc_id, game_id])
    db.commit()
    cur = db.execute("select * from acc_game")
    j = cur.fetchall()


    if i == j:
        return "fail"
    return redirect(url_for('cart', name=name))


@app.route('/cart/')
def cart():
    name = request.args.get("name")
    db = get_db()
    cursor = db.execute("select id from accounts where name == ?", [name])
    id = cursor.fetchone()
    cursor = db.execute("select acc_id,game_id from acc_game")
    acc_game = cursor.fetchall()
    cursor = db.execute("select id,name,desc,price,img_key,type from games")
    games = cursor.fetchall()
    games_cart = []
    for row in acc_game:
        if row[0] == id[0]:
            for game in games:
                if game[0] == row[1]:
                    games_cart.append(game)
    total = 0
    for g in games_cart:
        total += g[3]
    return render_template('cart.html', name=name, logged=True, games=games_cart, total=total, acc_id=id[0])


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
