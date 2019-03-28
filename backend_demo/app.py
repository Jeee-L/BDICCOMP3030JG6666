from flask import Flask,render_template,url_for,request,redirect,g,session
import config
import os
from datetime import timedelta


app = Flask(__name__)
# app.config.from_object(config)

app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def home():
    # username = session['username']
    # if session['username'] != None:
    # if username != None:
    #     return redirect('/1/')
    # else:
        return redirect('/0/')

@app.route('/<is_login>/')
def home_page(is_login):
    if is_login == '1':
        return render_template('homepage.html',user=session['username'])
    else:
        return render_template('homepage.html')

@app.route('/login/',methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        session['username'] = username
        app.config['PERMANENT_SESSION_TIME'] = timedelta(days=7)
        session.permanent = True

        # search in the database to check whether this user is valid
        return redirect('/1/')
    else:
        return render_template('loginpage.html')

@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phonenumber']
        email = request.form['email']
        check_password = request.form['check_password']
        print("username: "+username+" password: "+password)
        if check_password == password and password != '':
            # search in database
            return redirect(url_for('success_page'))
        else:
            return redirect(url_for('failure_page'))
    else:
        return render_template('registerpage.html')

@app.route('/success/')
def success_page():
    return render_template('successpage.html')

@app.route('/failure/')
def failure_page():
    return render_template('register_failpage.html')

@app.route('/deatil/',methods=['GET','POST'])
def detail_page():
    if request.method == 'POST':
        altered_username = request.form['alteredname']
        altered_password = request.form['alteredpassword']
        altered_phone = request.form['alteredphone']
        altered_email = request.form['alteredemail']
        return render_template('successpage.html')
    else:
        return render_template('detail.html')

@app.route('/logout/')
def logout_page():
    return render_template('loginpage.html')

if __name__ == '__main__':
    app.run()
