from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import yaml



app = Flask(__name__)
db = yaml.load(open('/var/Project/www/db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(namea, email) VALUES(%s,%s)" , ( name , email ))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('test.html')


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)
