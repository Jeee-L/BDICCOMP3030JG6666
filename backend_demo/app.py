from flask import Flask, render_template, request, redirect, session, jsonify, make_response
import os
import json
from datetime import timedelta
from email_verificatoin import email_verify
from flask_cors import CORS
from re_verification import *
import user
import employee
import administrator
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import yaml

from ext import db

app = Flask(__name__)
CORS(app, support_credentials=True)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=7)
app.send_file_max_age_default = timedelta(seconds=10)
# dbs = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)
dbs = yaml.load(open(
    r'/Users/pro13/Desktop/Study/3Junior/SecondSemester/SEP2/GitRepository/BDICCOMP3030JG6666/backend_demo/db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = dbs['sqlalchemy_database_uri_local']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


@app.route('/')
def home():
    # user.user_all_insurance()
    return render_template('homepage.html')
    # user = session.get('username')
    # if user:
    #     return redirect('/1/')
    # else:
    #     return redirect('/0/')


# TODO 登陆暂时完成
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_info = json.loads(request.get_data())
        name = login_info['username']
        password = login_info['password']
        if verify_username(name):
            return user.login(name, password)
        elif verify_employeename(name):
            return employee.login(name, password)
        elif verify_administrator_name(name):
            return administrator.login(name, password)
        else:
            return_value = {'state': '-1', 'error_msg': 'No such user'}
            return jsonify(return_value)


# TODO 用户注册暂时完成
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_info = json.loads(request.get_data())
        if register_info['verify'] == 0:
            verification_code = email_verify(register_info['email'])
            return verification_code
        else:
            return user.register(register_info)


# TODO 用户更改信息，头像，密码单独改
@app.route('/customer/info/', methods=['GET', 'POST'])
def customer_info():
    if request.method == 'POST':
        update_info = json.loads(request.get_data())
        return user.update_user_info(update_info)

@app.route('/customer/info/update_password',methods=['GET','POST'])
def customer_update_password():
    if request.method == 'POST':
        update_password = json.loads(request.get_data())
        if update_password['verify'] == 0:
            verification_code = email_verify(update_password['email'])
            return verification_code
        else:
            return user.update_password(update_password['username'],update_password['password'],update_password['confirm_password'])

@app.route('/customer/info/update_avatar',methods=['GET','POST'])
def customer_update_avatar():
    if request.method == 'POST':
        update_avatar = json.loads(request.get_data())
        return user.update_user_image(update_avatar['username'],update_avatar['image'])

# TODO 待测试
@app.route('/luggage/order/create', methods=['GET', 'POST'])
def luggage_order_create():
    if request.method == 'POST':
        insurance_info = json.loads(request.get_data())
        # print(insurance_info)
        return user.buy_insurance(insurance_info)


@app.route('/luggage/order/list', methods=['GET', 'POST'])
def luggage_order_list():
    if request.method == 'POST':
        claim_info = json.loads(request.get_data())
        if claim_info['check'] == '0':
            return user.user_all_insurance_order(claim_info['username'])
        else:
            return user.apply_claim(claim_info)


@app.route('/luggage/order/new_travel', methods=['GET', 'POST'])
def new_travel():
    if request.method == 'POST':
        supplementary_information = json.loads(request.get_data())
        return user.supplementary_information(supplementary_information)

@app.route('/list_user_all_insurance_order',methods=['GET','POST'])
def list_user_all_insurance_order():
    if request.method == 'POST':
        username = json.loads(request.get_data())
        return user.user_all_insurance_order(username)

@app.route('/list_user_all_claim',methods=['GET','POST'])
def list_user_all_claim():
    if request.method == 'POST':
        username = json.loads(request.get_data())
        return user.user_all_claim(username)

@app.route('/logout/')
def logout_page():
    if request.method == 'POST':
        session.clear()  # TODO 用户登出要清cookie和session
        return None

@app.route('/all_customers/',methods=['GET','POST'])
def all_customers():
    if request.method == 'POST':
        return user.all_users()


# TODO 员工更改密码暂时完成
@app.route('/employee_update_password/', methods=['GET', 'POST'])
def employee_update_password_page():
    if request.method == 'POST':
        employee_update_info = json.loads(request.get_data())
        return employee.update_password(employee_update_info)


# TODO 员工是否应该看到所有的保险和理赔申请？
@app.route('/check_all_insurance/', methods=['GET', 'POST'])
def list_all_insurance_page():
    if request.method == 'POST':
        return employee.list_all_insurance()


@app.route('/list_all_claim/', methods=['GET', 'POST'])
def list_all_claim_page():
    if request.method == 'POST':
        return employee.list_all_claim()

@app.route('/list_insurance_order_info/', methods=['GET', 'POST'])
def list_insurance_order_info_page():
    if request.method == 'POST':
        insurance_order_id = json.loads(request.get_data())
        return employee.insurance_order_detail(insurance_order_id)


# TODO 员工处理理赔申请暂时完成，需要前端传来员工受理意见(即state)
@app.route('/address_claim/', methods=['GET', 'POST'])
def address_claim_page():
    if request.method == 'POST':
        address_info = json.loads(request.get_data())
        return employee.address_claim(address_info)

@app.route('/all_employees/',methods=['GET','POST'])
def all_employees():
    if request.method == 'POST':
        return employee.all_employees()

@app.route('/administrator_update_password/', methods=['GET', 'POST'])
def administrator_update_password():
    if request.method == 'POST':
        administrator_info = json.loads(request.get_data())
        return administrator.update_password(administrator_info)


@app.route('/create_new_administrator/', methods=['GET', 'POST'])
def create_new_administrator():
    if request.method == 'POST':
        new_administrator_info = json.loads(request.get_data())
        return administrator.create_new_administrator(new_administrator_info)


@app.route('/delete_administrator/', methods=['GET', 'POST'])
def delete_administrator():
    if request.method == 'POST':
        delete_info = json.loads(request.get_data())
        return administrator.delete_administrator(delete_info)


@app.route('/create_employee/', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        employee_info = json.loads(request.get_data())
        return administrator.create_employee(employee_info)


@app.route('/delete_employee/', methods=['GET', 'POST'])
def delete_employee():
    if request.method == 'POST':
        delete_employee_id = json.loads(request.get_data())
        return administrator.delete_employee(delete_employee_id)


@app.route('/update_employee_password/', methods=['GET', 'POST'])
def update_employee_password():
    if request.method == 'POST':
        update_employee_info = json.loads(request.get_data())
        return administrator.update_employee_password(update_employee_info)


@app.route('/create_user/', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        create_user_info = json.loads(request.get_data())
        return administrator.create_user(create_user_info)

@app.route('/delete_user/', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        delete_username = json.loads(request.get_data())
        return administrator.delete_user(delete_username)


@app.route('/update_user_password/', methods=['GET', 'POST'])
def update_user_password():
    if request.method == 'POST':
        update_user_info = json.loads(request.get_data())
        return administrator.update_user_password(update_user_info)


if __name__ == '__main__':
    app.run()
