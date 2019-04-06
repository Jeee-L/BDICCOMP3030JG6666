from flask import Flask,render_template,url_for,request,redirect,g,session,jsonify,make_response
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta
from email_verificatoin import email_verify
from flask_cors import core
import user

# TODO 所有的状态：0--未处理，1--处理中，2--处理结束

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=7)
app.send_file_max_age_default = timedelta(seconds=10)


@app.route('/')
def home():
    user = session.get('username')
    if user:
        return redirect('/1/')
    else:
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
        confirm_password = request.form['comfirm_password']
        return user.login(username,password,confirm_password)


@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        register_info = {}
        register_info['name'] = request.form['username']
        register_info['password'] = request.form['password']
        register_info['confirm_password'] = request.form['confirm_password']
        register_info['passport_num'] = request.form['passport']
        register_info['phone_num'] = request.form['phonenumber']
        register_info['email'] = request.form['email']
        return user.register(register_info)


@app.route('/info/',methods=['GET','POST'])
def info_page():
    if request.method == 'POST':
        update_info = {}
        update_info['old_name'] = request.form['old_name']
        update_info['new_name'] = request.form['update_name']
        update_info['password'] = request.form['update_password']
        update_info['confirm_password'] = request.form['update_confirm_password']
        update_info['passport_num'] = request.form['update_passport']
        update_info['phone_num'] = request.form['update_phone']
        update_info['email'] = request.form['update_email']

        user_image = request.files['user_image']

        # TODO 所有信息同时更新还是可以分开更新？
        # user.update_name(update_info['old_name'],update_info['new_name'])
        # user.update_password(update_info['old_name'],update_info['password'],update_info['confirm_password'])
        # user.update_passport(update_info['old_name'],update_info['passport_num'])
        # user.update_email(update_info['old_name'],update_info['email'])
        # user.update_phone(update_info['old_name'],update_info['phone_num'])
        # user.update_user_image(update_info['old_name'],user_image)
        return None

@app.route('/buy_insurance/',methods=['GET','POST'])
def buy_insurance_page():
    if request.method == 'POST':
        insurance_info = {}
        insurance_info['username'] = request.form['username']
        insurance_info['product_id'] = request.form['product_id']
        insurance_info['amount_of_money'] = request.form['amount_of_money']
        insurance_info['flight_number'] = request.form['flight_number']
        insurance_info['status'] = 0    # 0-未处理
        insurance_info['image'] = request.files['insurance_image']

        return user.buy_insurance(insurance_info)


@app.route('/apply_claim/',methods=['GET','POST'])
def apply_claim_page():
    if request.method == 'POST':
        claim_info = {}
        claim_info['insurance_id'] = request.form['insurance_id']
        claim_info['employee_id'] = -1 # 表示新的订单，没有员工处理
        claim_info['reason'] = request.form['reason']
        claim_info['status'] = 0

        return user.apply_claim(claim_info)

@app.route('/email_verification/',methods=['GET','POST'])
def email_verification_page():
    if request.method == 'POST':
        user_email = request.form['email_address']
        verification_code = email_verify(user_email)
        return None

@app.route('/logout/')
def logout_page():
    session.clear() # TODO 用户登出要清cookie和session
    return None


if __name__ == '__main__':
    app.run()
