from flask import Flask,render_template,request,redirect,session,jsonify,make_response
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

app = Flask(__name__)
CORS(app,support_credentials=True)

db = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=7)
app.send_file_max_age_default = timedelta(seconds=10)


# @app.route('/')
# def home():
#     user = session.get('username')
#     if user:
#         return redirect('/1/')
#     else:
#         return redirect('/0/')
#
# @app.route('/<is_login>/')
# def home_page(is_login):
#     if is_login == '1':
#         return render_template('homepage.html',user=session['username'])
#     else:
#         return render_template('homepage.html')

# TODO 登陆暂时完成
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_info = json.loads(request.get_data())
        name = login_info['username']
        password = login_info['password']
        if verify_username(name):
            return user.login(name,password)
        elif verify_employeename(name):
            return employee.login(name,password)
        elif verify_administrator_name(name):
            return administrator.login(name,password)
        else:
            return_value = {'state': '-1', 'error_msg': 'No such user'}
            return jsonify(return_value)

# TODO 用户注册暂时完成
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        register_info = json.loads(request.get_data())
        if register_info['verify'] == 0:
            verification_code = email_verify(register_info['email'])
            return verification_code
        else:
            return user.register(register_info)

# TODO 用户更改信息暂时完成，头像未完成
@app.route('/customer/info/',methods=['GET','POST'])
def customer_info():
    if request.method == 'POST':
        update_info = json.loads(request.get_data())
        return user.update_user_info(update_info)

@app.route('/luggage/order/create',methods=['GET','POST'])
def luggage_order_create():
    if request.method == 'POST':
        insurance_info = {}
        insurance_info['first_name'] = request.form['first_name']
        insurance_info['last_name'] = request.form['last_name']
        insurance_info['user_name'] = request.form['user_name']
        insurance_info['passport_id'] = request.form['passport_id']
        insurance_info['mobile_cn'] = request.form['mobile_cn']
        insurance_info['email'] = request.form['email']
        insurance_info['birthday'] = request.form['birthday']
        insurance_info['address'] = request.form['address']

        insurance_info['product_id'] = request.form['product_id']
        insurance_info['project_id'] = request.form['project_id']
        insurance_info['flight_number'] = request.form['flight_number']

        insurance_info['status'] = 0    # 0-未处理

        insurance_info['luggage_image_outside'] = request.files['luggage_image_outside']
        insurance_info['luggage_image_inside'] = request.files['luggage_image_inside']
        insurance_info['luggage_height'] = request.files['luggage_height']
        insurance_info['luggage_width'] = request.files['luggage_width']

        insurance_info['remark'] = request.files['remark']

        return user.buy_insurance(insurance_info)

@app.route('/luggage/order/list',methods=['GET','POST'])
def luggage_order_list():
    if request.method == 'POST':
        claim_info = {}
        claim_info['order_id'] = request.form['order_id']
        claim_info['user_name'] = request.form['user_name']
        claim_info['lost_time'] = request.form['lost_time']
        claim_info['lost_place'] = request.form['lost_place']
        claim_info['flight_number'] = request.form['flight_number']
        claim_info['lost_reason'] = request.form['lost_reason']
        claim_info['remark'] = request.form['remark']
        claim_info['employee_id'] = -1  # 表示新的订单，没有员工处理
        claim_info['status'] = -1

        return user.apply_claim(claim_info)

@app.route('/apply_claim/',methods=['GET','POST'])
def apply_claim_page():
    if request.method == 'POST':
        claim_info = {}
        claim_info['insurance_id'] = request.form['insurance_id']
        claim_info['employee_id'] = -1 # 表示新的订单，没有员工处理
        claim_info['reason'] = request.form['reason']
        claim_info['status'] = -1

        return user.apply_claim(claim_info)

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
    # state = request.form['state']
    audit_result = request.form['audit_result']
    return employee.address_claim(claim_id,audit_result)

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


if __name__ == '__main__':
    app.run()
