from flask import Flask,render_template,url_for,request,redirect,session,jsonify,make_response
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta
from email_verificatoin import email_verify
from flask_cors import core
import user
import employee
import administrator

# TODO 所有的状态：0--未处理，1--处理中，2--驳回， 3--处理结束

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

@app.route('/user_login/',methods=['GET','POST'])
def user_login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return user.login(username,password)


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


@app.route('/user_info/',methods=['GET','POST'])
def user_info_page():
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
        # user.update_password(update_info['old_name'],,update_info['password'],update_info['confirm_password'])
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

@app.route('/employee_login/',methods=['GET','POST'])
def employee_lonin_page():
    employeeid = request.form['employeeid']
    password = request.form['password']
    return employee.login(employeeid, password)

@app.route('/employee_update_password/',methods=['GET','POST'])
def employee_update_password_page():
    employeeid = request.form['employeeid']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    return employee.update_password(employeeid,new_password,confirm_password)

# TODO 员工是否应该看到所有的保险和理赔申请？
@app.route('/check_all_insurance/',methods=['GET','POST'])
def list_all_insurance_page():
    return employee.list_all_insurance()

@app.route('/list_all_claim/',methods=['GET','POST'])
def list_all_claim_page():
    return employee.list_all_claim()

@app.route('/address_claim/',methods=['GET','POST'])
def address_claim_page():
    claim_id = request.form['claim_id']
    # TODO 这里的状态位如何确定？
    state = request.form['state']
    return employee.address_claim(claim_id,state)

@app.route('/administrator_login/',methods=['GET','POST'])
def administrator_login_page():
    administratorid = request.form['administratorid']
    password = request.form['password']
    return administrator.login(administratorid, password)

@app.route('/administrator_update_password/',methods=['GET','POST'])
def administrator_update_password():
    administratorid = request.form['administratorid']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    return administrator.update_password(administratorid, new_password, confirm_password)

@app.route('/create_new_administrator/',methods=['GET','POST'])
def create_new_administrator():
    new_id = request.form['new_id']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    return administrator.create_new_administrator(new_id,password,confirm_password)

@app.route('/delete_administrator/',methods=['GET','POST'])
def delete_administrator():
    current_id = request.form['current_id']
    delete_id = request.form['delete_id']
    return administrator.delete_administrator(current_id,delete_id)

@app.route('/create_employee/',methods=['GET','POST'])
def create_employee():
    employee_id = request.form['employee_id']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    return administrator.create_employee(employee_id, password, confirm_password)

@app.route('/delete_employee/',methods=['GET','POST'])
def delete_employee():
    delete_employee_id = request.form['delete_employee_id']
    return administrator.delete_employee(delete_employee_id)

@app.route('/update_employee_password/',methods=['GET','POST'])
def update_employee_password():
    update_employee_id = request.form['update_employee_id']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    return administrator.update_employee_password(update_employee_id,password,confirm_password)

@app.route('/delete_user/',methods=['GET','POST'])
def delete_user():
    delete_username = request.form['delete_username']
    return administrator.delete_user(delete_username)

# TODO list
"""
1. administrator 是否看到所有的claim和insurance，是否可以和员工共用一个方法？(再一个py文件)
2. administrator 的名字问题，a@开头
3. 员工和管理员的名字前缀(e@,a@),应不应该手动输入
4. 其他信息的正则验证
5. 状态位的确定
"""

if __name__ == '__main__':
    app.run()
