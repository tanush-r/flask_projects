from flask import Flask, render_template,url_for,request,session,redirect
import mysql.connector
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home',methods=["POST"])
def home():
    name = request.form['name']
    age = request.form['age']
    location = request.form['location']
    password = request.form['password']
    mycon = mysql.connector.connect(host="localhost",
                                    database="ps5_login_info",
                                    user="root",
                                    passwd="root",
                                    auth_plugin='mysql_native_password')
    cursor = mycon.cursor()
    cursor.execute("insert into accounts(name,age,location,password) values ('{}',{},'{}','{}')".format(name,age,location,password))
    mycon.commit()
    cursor.close()
    return render_template('home.html',name=name,logged=True)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html',check=False)

@app.route('/processed', methods=['POST'])
def processed():
    name = request.form['name']
    password = request.form['password']
    mycon = mysql.connector.connect(host="localhost",
                                    database="ps5_login_info",
                                    user="root",
                                    passwd="root",
                                    auth_plugin='mysql_native_password')
    cursor = mycon.cursor()
    cursor.execute("select name,password from accounts")
    data = cursor.fetchall()
    print(data)
    for row in data:
        if row[0] == name and row[1] == password:
            return render_template('home.html', name=name, logged=True)
    return render_template('signin.html', check=True)




if __name__ == '__main__':
    app.run(debug=False)
