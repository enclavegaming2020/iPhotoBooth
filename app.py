from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector as ms
import re
from werkzeug.utils import secure_filename

conn = ms.connect(host = "sql.freedb.tech", user = "freedb_user_database", password = "CVkej7hsu7bcR#F", database="freedb_photobooth")
app = Flask(__name__)

app.secret_key = "your secret key"

@app.route('/')
@app.route('/login', methods = ['GET' , 'POST'])

def login():
    msg = ""
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor1= conn.cursor()
        cursor1.execute("select * from account where username = %s and ipassword = %s",(username,password,))
        row = cursor1.fetchone()
        if row:
            session['loggedin'] = True
            session['username'] = row[3]
            msg = 'Logged in Successfully'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password ! '
    return render_template('login.html', msg=msg)

@app.route('/register', methods = ['GET', 'POST'])

def register():
    msg = ''
    if request.method == "POST" and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['signup-username']
        password = request.form['signup-password']
        cursor2 = conn.cursor()
        cursor2.execute("select * from account where username = %s",(username,))
        data = cursor2.fetchone()
        if data:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Invalid email address !"
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = "Please fill out the form !"     
        else:
            cursor3 = conn.cursor()
            cursor3.execute("insert into account values(%s,%s,%s,%s,%s)",(firstname,lastname,email,username,password,))
            conn.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = "Please fill out the form"

    return render_template("login.html", msg = msg)

@app.route("/user")

def user():
    return render_template("login.html")

@app.route("/forgot_password")

def forgot_password():
    return render_template("mail.html")

@app.route("/mail",methods=['POST','GET'])

def mail():
    global iemail
    if request.method == "POST" and 'email' in request.form:
        iemail = request.form['email']
        cursor4 = conn.cursor()
        cursor4.execute("select * from account where email = %s",(iemail,))
        data = cursor4.fetchone()
        cursor4.close()
        cursor4.reset()
        if data:
            return render_template("forgot.html")
        else:
            return render_template("login.html", msg="Email Id not found")
                
@app.route("/forgot",methods=['POST','GET'])

def forgot():
    if request.method == "POST" and 'password' in request.form:
        password = request.form['password']
        cursor5 = conn.cursor()
        cursor5.execute("update account set ipassword = %s where email = %s",(password,iemail,))
        conn.commit()
        return render_template("login.html", msg="Password updated successfully")
    
@app.route("/upload", methods = ['POST'])

def upload():
    if request.method == 'POST':
        file = request.files['dragfile']
        file.save(f"photobooth\\uploads\\{file.filename}")
        return render_template("index.html", msg="File uploaded successfully")

if __name__ == "__main__":
    app.run(debug=True)