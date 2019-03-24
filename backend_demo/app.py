from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/login/',methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # search in the database to check whether this user is valid
        return redirect(url_for('detail_page'))
    else:
        return render_template('loginpage.html')

@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
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

@app.route('/deatil/')
def detail_page():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run()
