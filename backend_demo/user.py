from re_verification import *
from flask import jsonify
import db_operation.users_operate as db_usr_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr
import db_operation.order as db_ord_opr
import os
import cv2
from werkzeug.utils import secure_filename


def login(username, password):
    if db_usr_opr.search_username(username) is None:
        return_value = {'state': '-1', 'error_msg': 'No such user'}
        return jsonify(return_value)
    elif not (db_usr_opr.password_is_right(username, password)):
        return_value = {'state': '0', 'error_msg': 'Password is not correct'}
        return jsonify(return_value)
    else:
        return user_all_info(username)


def user_all_info(username):
    user = db_usr_opr.search_username(username)
    return_value = {
        'state': '1',
        'username':username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_num': user.phone_num,
        'passport_num': user.passport_num,
        'email': user.email,
        'birthday': user.birthday,
        'address': user.address,
        'insurance_list': user_all_insurance(username),
        'insurance_order_list': user_all_insurance_order(username),
        'claim_list': user_all_claim(username)
    }
    return jsonify(return_value)


def user_all_insurance(username):
    insurance_list = db_usr_opr.get_insurance(username)
    if insurance_list is []:
        return ""
    else:
        return_list = []
        for insurance in insurance_list:
            insurance_dict = {}  # TODO 可能会有问题，也许会每次循环都加一遍
            insurance_dict['username'] = insurance.username
            insurance_dict['id'] = insurance.id
            insurance_dict['project_id'] = insurance.project_id
            insurance_dict['product_id'] = insurance.product_id
            insurance_dict['amount_of_money'] = insurance.amount_of_money
            insurance_dict['compensated_amount'] = insurance.compensated_amount
            insurance_dict['status'] = insurance.status
            insurance_dict['date'] = insurance.date
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
            claim_dict['insurance_id'] = claim.insurance_id
            claim_dict['id'] = claim.id
            claim_dict['employee_id'] = claim.employee_id
            claim_dict['reason'] = claim.reason
            claim_dict['status'] = claim.status
            claim_dict['lost_time'] = claim.lost_time
            claim_dict['lost_place'] = claim.lost_place
            claim_dict['date'] = claim.time
            claim_dict['remark'] = claim.remark
            return_list.append(claim_dict)
        return return_list


def user_all_insurance_order(username):
    order_list = db_usr_opr.get_order(username)
    if order_list is []:
        return ""
    else:
        return_list = []
        for order in order_list:
            order_dict = {}
            order_list['order_id'] = order.order_id
            order_list['state'] = order.state
            order_list['username'] = order.username
            order_list['insurance_id'] = order.insurance_id
            order_list['flight_number'] = order.flight_number
            order_list['luggage_image_outside'] = order.luggage_image_outside
            order_list['luggage_image_inside'] = order.luggage_image_inside
            order_list['luggage_height'] = order.luggage_height
            order_list['luggage_width'] = order.luggage_width
            order_list['date'] = order.date
            order_list['claim_id'] = order.claim_id
            order_list['remark'] = order.remark
            return_list.append(order_dict)
        return return_list


def register(register_info):
    verify_result = verify_register_info(register_info)
    if verify_result == True:
        try:
            success_message = 'Create successfully'
            return_message = db_usr_opr.insert_user(register_info)
            if success_message == return_message:
                return_value = {'state': '1'}
                return jsonify(return_value)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)
    else:
        return verify_result


def verify_register_info(register_info):
    if not verify_username(register_info['username']):
        return_value = {'state': '0', 'error_msg': "Illegal username"}
        return jsonify(return_value)
    elif not (register_info['password'] == register_info['confirm_password']):
        return_value = {'state': '0', 'error_msg': "Two password are different"}
        return jsonify(return_value)
    elif not verify_password(register_info['password']):
        return_value = {'state': '0', 'error_msg': "Illegal password"}
        return jsonify(return_value)
    elif not verify_email(register_info['email']):
        return_value = {'state': '0', 'error_msg': "Illegal email"}
        return jsonify(return_value)
    elif not verify_phone_number(register_info['phone_num']):
        return_value = {'state': '0', 'error_msg': "Illegal phone number"}
        return jsonify(return_value)
    else:
        return True


def update_user_info(update_info):
    update_first_name(update_info['old_username'], update_info['first_name'])
    update_last_name(update_info['old_username'], update_info['last_name'])
    update_name(update_info['old_username'], update_info['username'])
    update_password(update_info['old_username'], update_info['password'], update_info['confirm_password'])
    update_email(update_info['old_username'], update_info['email'])
    update_phone(update_info['old_username'], update_info['phone_num'])
    update_passport(update_info['old_username'], update_info['passport_num'])
    update_birthday(update_info['old_username'], update_info['birthday'])
    update_address(update_info['old_username'], update_info['address'])
    update_user_image(update_info['old_username'], update_info['image'])

    return_value = {'state': '1'}
    return jsonify(return_value)


def update_first_name(username, first_name):
    user = db_usr_opr.search_username(username)
    if not (user is None):
        user.first_name = first_name
    else:
        return_value = {'state': '0', 'error_msg': 'No such user'}
        return jsonify(return_value)


def update_last_name(username, last_name):
    user = db_usr_opr.search_username(username)
    if not (user is None):
        user.last_name = last_name
    else:
        return_value = {'state': '0', 'error_msg': 'No such user'}
        return jsonify(return_value)


def update_birthday(username, birthday):
    user = db_usr_opr.search_username(username)
    if not (user is None):
        user.birthday = birthday
    else:
        return_value = {'state': '0', 'error_msg': 'No such user'}
        return jsonify(return_value)


def update_address(username, address):
    user = db_usr_opr.search_username(username)
    if not (user is None):
        user.address = address
    else:
        return_value = {'state': '0', 'error_msg': 'No such user'}
        return jsonify(return_value)


def update_name(old_name, new_name):
    if not verify_username(new_name):
        return_value = {'state': '0', 'error_msg': 'Illegal username'}
        return jsonify(return_value)
    else:
        try:
            db_usr_opr.update_username(old_name, new_name)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)


def update_password(name, new_password, confirm_password):
    # TODO 用邮箱验证来改密码？
    if not verify_password(new_password):
        return_value = {'state': '0', 'error_msg': 'Illegal password'}
        return jsonify(return_value)
    elif not (new_password == confirm_password):
        return_value = {'state': '0', 'error_msg': 'Two passwords are different'}
        return jsonify(return_value)
    else:
        try:
            db_usr_opr.update_password(name, new_password)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)


def update_email(name, new_email):
    if not verify_email(new_email):
        return_value = {'state': '0', 'error_msg': 'Illegal email'}
        return jsonify(return_value)
    else:
        try:
            db_usr_opr.update_email(name, new_email)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)


def update_phone(name, new_phone):
    if not verify_phone_number(new_phone):
        return_value = {'state': '0', 'error_msg': 'Illegal phone number'}
        return jsonify(return_value)
    else:
        try:
            db_usr_opr.update_phone_num(name, new_phone)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)


def update_passport(name, new_passport):
    if not verify_passport(new_passport):
        return_value = {'state': '0', 'error_msg': 'Illegal passport number'}
        return jsonify(return_value)
    else:
        try:
            db_usr_opr.update_passport_num(name, new_passport)
        except AssertionError as ae:
            return_value = {'state': '0', 'error_msg': ae}
            return jsonify(return_value)


# 图片允许的后缀名
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#
#
# def img_stream(img_local_path):
#     """
#     工具函数:
#     获取本地图片流
#     :param img_local_path:文件单张图片的本地绝对路径
#     :return: 图片流
#     """
#     import base64
#     img_stream = ''
#     with open(img_local_path, 'r') as img_f:
#         img_stream = img_f.read()
#         img_stream = base64.b64encode(img_stream)
#     return img_stream


def update_user_image(name, user_image):
    # if not (user_image and allowed_file(user_image.filename)):
    #     return jsonify({"state": '0', "error_msg": "Illegal image type，limited: png、PNG、jpg、JPG、bmp"})
    # basepath = os.path.dirname(__file__)  # 当前文件所在路径
    #
    # # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    # upload_path = os.path.join(basepath, 'static/user_images',
    #                            secure_filename(user_image.filename))
    # user_image.save(upload_path)
    #
    # byte_size = os.path.getsize(upload_path)
    # MB_size = float(byte_size / (1024 * 1024))
    # if not (MB_size < 2):
    #     return jsonify({"state": '0', "error_msg": "image size should not bigger than 2 MB"})
    #
    # # 使用Opencv转换一下图片格式和名称
    # img = cv2.imread(upload_path)
    # cv2.imwrite(os.path.join(basepath, 'static/user_images', 'temp_user_avatar.jpg'), img)
    #
    # image_stream = img_stream(basepath + 'static/user_images/temp_user_avatar')

    if len(user_image) > 204800:
        return jsonify({"state": '0', "error_msg": "Image size should not bigger than 2 MB"})
    try:
        db_usr_opr.update_profile(name, user_image)
        # os.remove(upload_path)
        # return "头像上传成功"
        return jsonify({"state":"1"})
    except AssertionError as ae:
        return jsonify({"state": '0', "error_msg": ae})


def buy_insurance(insurance_info):
    insurance_info['status'] = 0
    try:
        insurance_id = db_ins_opr.add_insurance(insurance_info)
        return jsonify({'state': '1', 'insurance_id': insurance_id})
    except AssertionError as ae:
        return jsonify({'state': '0', 'error_msg': ae})


def apply_claim(claim_info):
    claim_info['employee_id'] = -1  # 表示新的订单，没有员工处理
    claim_info['status'] = -1

    if not (len(claim_info['reason']) < 300):
        return jsonify({'state': '0', 'error_msg': 'The length of reason should less than 300 characters'})
    try:
        # TODO 改state，待测试
        corresponded_order_id = claim_info['order_id']
        corresponded_order = db_ord_opr.search_order(corresponded_order_id)
        corresponded_order.state = 0
        db_cla_opr.add_claim(claim_info)
        return jsonify({'state': '1'})
    except AssertionError as ae:
        return jsonify({'state': '0', 'error_msg': ae})


# 用户添加保险信息
def supplementary_information(supplementary_info):
    supplementary_info['state'] = -1
    if len(supplementary_info['luggage_image_outside'])>204800 or len(supplementary_info['luggage_image_inside'])>204800:
        return jsonify({"state": '0', "error_msg": "Image size should not bigger than 2 MB"})
    try:
        db_ord_opr.add_order(supplementary_info)
        return jsonify({'state': '1'})
    except AssertionError as ae:
        return jsonify({'state': '0', 'error_msg': ae})
