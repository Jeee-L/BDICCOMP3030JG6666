from re_verification import *
from flask import jsonify
import db_operation.users_operate as db_usr_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr
import db_operation.order as db_ord_opr
import db_operation.product_operate as db_duct_opr
import db_operation.project_operate as db_ject_opr
from datetime import datetime
from email_verificatoin import email_verify
import time

def login(username, password):
    if db_usr_opr.search_username(username) is None:
        return jsonify({'state': '-1', 'error_msg': 'No such user'})
    elif not (db_usr_opr.password_is_right(username, password)):
        return jsonify({'state': '0', 'error_msg': 'Password is not correct'})
    else:
        return user_all_info(username)


def user_all_info(username):
    user = db_usr_opr.search_username(username)
    birthday_date = user.birthday
    if birthday_date is not None:
        birthday_date = birthday_date.strftime("%Y-%m-%d")

    return_value = {
        'state': '1',
        'username':username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_num': user.phone_num,
        'passport_num': user.passport_num,
        'email': user.email,
        'birthday': birthday_date,
        'address': user.address,
        'insurance_list': user_all_insurance(username),
        # 'insurance_order_list': user_all_insurance_order(username),
        # 'claim_list': user_all_claim(username)
    }
    return jsonify(return_value)


def user_all_insurance(username):
    insurance_list = db_usr_opr.get_insurance(username)
    if insurance_list is []:
        return ""
    else:
        return_list = []
        for insurance in insurance_list:
            insurance_dict = {}
            insurance_dict['username'] = insurance.username
            insurance_dict['id'] = str(insurance.id)
            insurance_dict['amount_of_money'] = str(insurance.amount_of_money)
            insurance_dict['compensated_amount'] = str(insurance.compensated_amount)
            insurance_dict['state'] = str(insurance.state)
            insurance_dict['date'] = insurance.date.strftime("%Y-%m-%d")
            insurance_dict['remark'] = insurance.remark
            return_list.append(insurance_dict)
        return return_list


def user_all_claim(username):
    claim_list = db_usr_opr.get_claim(username)
    if claim_list is []:
        return ""
    else:
        return_list = []
        for claim in claim_list:
            claim_dict = {}
            claim_dict['username'] = username # claim表里没有username，所以这种返回
            claim_dict['insurance_id'] = str(claim.insurance_id)
            claim_dict['id'] = str(claim.id)
            claim_dict['employee_id'] = str(claim.employee_id)
            claim_dict['reason'] = claim.reason
            claim_dict['state'] = str(claim.state)
            claim_dict['lost_time'] = claim.lost_time
            claim_dict['lost_place'] = claim.lost_place
            claim_dict['date'] = claim.time.strftime("%Y-%m-%d")
            claim_dict['remark'] = claim.remark
            return_list.append(claim_dict)
        return jsonify(return_list)


def user_all_insurance_order(username):
    order_list = db_usr_opr.get_order(username['username'])
    if order_list is []:
        return ""
    else:
        return_list = []
        for order in order_list:
            order_dict = {}
            order_dict['insurance_order_id'] = str(order.order_id)
            order_dict['state'] = str(order.state)
            order_dict['username'] = order.username
            order_dict['insurance_id'] = str(order.insurance_id)
            order_dict['flight_number'] = order.flight_number
            order_dict['luggage_image_outside'] = order.luggage_image_outside
            order_dict['luggage_image_inside'] = order.luggage_image_inside
            order_dict['luggage_height'] = order.luggage_height
            order_dict['luggage_width'] = order.luggage_width
            order_dict['date'] = order.date.strftime("%Y-%m-%d")
            corresponded_claims = order.claim_id
            claim_ids = []
            for claim in corresponded_claims:
                claim_ids.append(str(claim.id))
            order_dict['claim_id'] = claim_ids
            order_dict['remark'] = order.remark
            order_dict['sumPrice'] = str(order.sumPrice)
            select_img_list = db_ord_opr.select_img(order.order_id)
            select_img_return_list = []
            for select_img in select_img_list:
                select_img_dict = {}
                select_img_dict['imgUrl'] = select_img.imgUrl
                select_img_dict['name'] = select_img.name
                select_img_dict['price'] = str(select_img.price)
                select_img_dict['remark'] = select_img.remark
                select_img_return_list.append(select_img_dict)
            order_dict['select_img'] = select_img_return_list
            return_list.append(order_dict)
        return jsonify(return_list)


def register(register_info):
    verify_result = verify_register_info(register_info)
    if verify_result == True:
        try:
            db_usr_opr.insert_user(register_info)
            return jsonify({'state': '1'})
        except AssertionError as ae:
            return jsonify({'state': '0', 'error_msg': 'Username already exist'})
    else:
        return verify_result


def verify_register_info(register_info):
    if not verify_username(register_info['username']):
        return jsonify({'state': '0', 'error_msg': "Illegal username"})
    elif not (register_info['password'] == register_info['confirm_password']):
        return jsonify({'state': '0', 'error_msg': "Two password are different"})
    elif not verify_password(register_info['password']):
        return jsonify({'state': '0', 'error_msg': "Illegal password"})
    elif not verify_email(register_info['email']):
        return jsonify({'state': '0', 'error_msg': "Illegal email"})
    elif not verify_phone_number(register_info['phone_num']):
        return jsonify({'state': '0', 'error_msg': "Illegal phone number"})
    else:
        return True


def update_user_info(update_info):
    update_first_name(update_info['old_username'], update_info['first_name'])
    update_last_name(update_info['old_username'], update_info['last_name'])
    update_email(update_info['old_username'], update_info['email'])
    update_phone(update_info['old_username'], update_info['phone_num'])
    update_passport(update_info['old_username'], update_info['passport_num'])
    update_birthday(update_info['old_username'], update_info['birthday'])
    update_address(update_info['old_username'], update_info['address'])
    # update_name(update_info['old_username'], update_info['username'])

    return jsonify({'state': '1'})


def update_first_name(username, first_name):
    if not (first_name is ''):
        try:
            db_usr_opr.update_first_name(username,first_name)
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg': 'No such user'})


def update_last_name(username, last_name):
    if not (last_name is ''):
        try:
            db_usr_opr.update_last_name(username,last_name)
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg': 'No such user'})


def update_birthday(username, birthday):
    if not (birthday is ''):
        birthday_date = datetime.strptime(birthday.split('T')[0], "%Y-%m-%d")
        try:
            db_usr_opr.update_birthday(username,birthday_date)
        except AssertionError as ae:
            return jsonify({'state': '0', 'error_msg': 'No such user'})


def update_address(username, address):
    if not (address is ''):
        try:
            db_usr_opr.update_address(username, address)
        except AssertionError as ae:
            return jsonify({'state': '0', 'error_msg': 'No such user'})


def update_name(old_name, new_name):
    if not ((new_name is '') and (old_name == new_name)):
        if not verify_username(new_name):
            return jsonify({'state': '0', 'error_msg': 'Illegal username'})
        else:
            try:
                db_usr_opr.update_username(old_name, new_name)
            except AssertionError as ae:
                if ae == "No such user":
                    return jsonify({'state': '0', 'error_msg': 'No such user'})
                elif ae == 'This name already exist':
                    return jsonify({'state': '0', 'error_msg': 'Username already exist'})

def send_verification_code(username):
    user = db_usr_opr.search_username(username)
    if user is None:
        return '0'
    email = user.email
    return email_verify(email)

def update_password(name, new_password, confirm_password):
    if not verify_password(new_password):
        return jsonify({'state': '0', 'error_msg': 'Illegal password'})
    elif not (new_password == confirm_password):
        return jsonify({'state': '0', 'error_msg': 'Two passwords are different'})
    else:
        try:
            db_usr_opr.update_password(name, new_password)
            return jsonify({'state':'1'})
        except AssertionError as ae:
            if ae == "No such user":
                return jsonify({'state': '0', 'error_msg': 'No such user'})
            elif ae == 'Same password':
                return jsonify({'state': '0', 'error_msg': 'The new password is same as the old one'})


def update_email(name, new_email):
    if not (new_email is ''):
        if not verify_email(new_email):
            return jsonify({'state': '0', 'error_msg': 'Illegal email'})
        else:
            try:
                db_usr_opr.update_email(name, new_email)
            except AssertionError as ae:
                return jsonify({'state': '0', 'error_msg': 'No such user'})


def update_phone(name, new_phone):
    if not (new_phone is ''):
        if not verify_phone_number(new_phone):
            return jsonify({'state': '0', 'error_msg': 'Illegal phone number'})
        else:
            try:
                db_usr_opr.update_phone_num(name, new_phone)
            except AssertionError as ae:
                return jsonify({'state': '0', 'error_msg': 'No such user'})


def update_passport(name, new_passport):
    if not (new_passport is ''):
        if not verify_passport(new_passport):
            return jsonify({'state': '0', 'error_msg': 'Illegal passport number'})
        else:
            try:
                db_usr_opr.update_passport_num(name, new_passport)
            except AssertionError as ae:
                return jsonify({'state': '0', 'error_msg': 'No such user'})

def update_user_image(name, user_image):
    try:
        db_usr_opr.update_profile(name, user_image)
        return jsonify({"state":"1"})
    except AssertionError as ae:
        return jsonify({"state": '0', "error_msg": 'No such user'})


def buy_insurance(insurance_info):
    insurance_info['state'] = 0
    insurance_info['compensated_amount'] = 0
    insurance_info['product_id'] = int(insurance_info['product_id'])
    insurance_info['project_id'] = int(insurance_info['project_id'])
    insurance_info['birthday'] = datetime.strptime(insurance_info['birthday'].split('T')[0], "%Y-%m-%d")
    corresponded_product = db_duct_opr.search_product(insurance_info['product_id'])
    insurance_info['duration'] = corresponded_product.product_information
    corresponded_project = db_ject_opr.search_project_object(insurance_info['product_id'],insurance_info['project_id'])
    insurance_info['amount_of_money'] = corresponded_project.coverage
    try:
        insurance_id = db_ins_opr.add_insurance(insurance_info)
        return jsonify({'state': '1', 'insurance_id': insurance_id})
    except AssertionError as ae:
        return jsonify({'state': '0', 'error_msg': 'No such user'})


def apply_claim(claim_info):
    claim_info['employee_id'] = -1  # 表示新的订单，没有员工处理
    claim_info['state'] = -2    # 初始状态 -2
    claim_info['lost_time'] = datetime.strptime(claim_info['lost_time'], "%Y-%m-%d")
    claim_info['order_id'] = int(claim_info['insurance_order_id'])

    if not (len(claim_info['reason']) < 300):
        return jsonify({'state': '0', 'error_msg': 'The length of reason should less than 300 characters'})
    if not (len(claim_info['remark']) < 300):
        return jsonify({'state': '0', 'error_msg': 'The length of remark should less than 300 characters'})
    if not (len(claim_info['lost_place']) < 100):
        return jsonify({'state': '0', 'error_msg': 'The length of lost place should less than 100 characters'})
    try:
        # 改对应insurance order 的 state
        db_ord_opr.change_state(claim_info['order_id'],0)
        db_cla_opr.add_claim(claim_info)
        return jsonify({'state': '1'})
    except AssertionError as ae:
        return jsonify({'state': '0', 'error_msg': 'No such order'})


# 用户添加保险信息
# 需要判断当前insurance是否已经达到赔付上限或逾期
# 如果没有，返回余额和剩余时间，如果是则返回错误信息
def supplementary_information(supplementary_info):
    supplementary_info['state'] = -1
    supplementary_info['luggage_width'] = int(supplementary_info['luggage_width'])
    supplementary_info['luggage_height'] = int(supplementary_info['luggage_height'])
    supplementary_info['sumPrice'] = int(supplementary_info['sumPrice'])

    # 算剩余金额
    # user = db_usr_opr.search_username(supplementary_info['username'])
    supplementary_info['insurance_id'] = db_usr_opr.get_first_insurance(supplementary_info['username'])
    corresponded_insurance = db_ins_opr.__search_insurance(supplementary_info['insurance_id'])
    remaining_amount = corresponded_insurance.amount_of_money - (corresponded_insurance.compensated_amount + supplementary_info['sumPrice'])

    # 算剩余时间
    current_date = datetime.now()
    begin_date = corresponded_insurance.date
    current_date.strftime("%Y-%m-%d")
    begin_date.strftime("%Y-%m-%d")
    day_gap = corresponded_insurance.duration - (current_date-begin_date).days

    if remaining_amount <= 0:
        return jsonify({'state':'0', 'error_msg':'Cumulative compensation has reached the upper limit of compensation'})
    elif day_gap <= 0:
        return jsonify({'state': '0', 'error_msg': 'This insurance is overdue'})
    else:
        try:
            order_id = db_ord_opr.add_order(supplementary_info)
            select_img_list = supplementary_info['select_img']
            for select_img in select_img_list:
                select_img['order_id'] = order_id
                try:
                    db_ord_opr.add_img(select_img)
                except AssertionError as iae:
                    return jsonify({'state': '0', 'error_msg': 'Unknown error'})
            return jsonify({'state': '1','remaining_money':remaining_amount,'remaining_time':day_gap})
        except AssertionError as ae:
            return jsonify({'state': '0', 'error_msg': 'No such user'})

def all_users():
    user_list = db_usr_opr.all()
    if user_list is []:
        return ""
    else:
        return_list = []
        for user in user_list:
            user_dict = {}
            user_dict['first_name'] = user.first_name
            user_dict['last_name'] = user.last_name
            user_dict['username'] = user.username
            user_dict['phone_num'] = user.phone_num
            user_dict['passport_num'] = user.passport_num
            user_dict['email'] = user.email
            birthday_str = datetime.strftime(user.birthday,"%Y-%m-%d")
            user_dict['birthday'] = birthday_str
            user_dict['address'] = user.first_name
            return_list.append(user_dict)
        return return_list