from re_verification import *
from flask import jsonify
import db_operation.users_operate as db_usr_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr
import db_operation.administrator_operate as db_adi_opr
import user

def login(administratorid,password):
    try:
        return_message = db_adi_opr.login(administratorid, password)
        success_message = 'Login successfully'
        if return_message == success_message:
            return_value = {'state': '3'}
            return jsonify(return_value)
    except AssertionError as ae:
        if ae == 'No such id':
            return_value = {'state': '-1','error_msg':'No such administrator'}
            return jsonify(return_value)
        elif ae == 'Password wrong':
            return_value = {'state': '0', 'error_msg': 'Password is not correct'}
            return jsonify(return_value)

def update_password(administrator_info):
    if not verify_password(administrator_info['new_password']):
        return jsonify({'stste':'0','error_msg':'Illegal password'})
    elif not (administrator_info['new_password'] == administrator_info['confirm_password']):
        return jsonify({'state':'0','error_msg':'Tow passwords are different'})
    else:
        try:
            db_adi_opr.update_password(administrator_info['administratorid'], administrator_info['new_password'])
            return jsonify({'state':'1'})
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg':ae})

def create_new_administrator(new_administrator_info):
    if not verify_password(new_administrator_info['password']):
        return jsonify({'stste':'0','error_msg':'Illegal password'})
    elif not (new_administrator_info['password'] == new_administrator_info['confirm_password']):
        return jsonify({'state':'0','error_msg':'Tow passwords are different'})
    elif not verify_administrator_name(new_administrator_info['id']):
        return jsonify({'stste':'0','error_msg':'Illegal administrator id'})
    else:
        try:
            db_adi_opr.create(new_administrator_info['id'], new_administrator_info['password'])
            return jsonify({'state':'1'})
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg':ae})

def delete_administrator(delete_info):
    if delete_info['current_id'] == delete_info['delete_id']:
        return jsonify({'stste':'0','error_msg':'Can not delete current account'})
    elif delete_info['delete_id'] == 'a@root': #TODO 管理员名字？
        return jsonify({'stste':'0','error_msg':'Can not delete root administrator'})
    else:
        try:
            db_adi_opr.delete(delete_info['delete_id'])
            return jsonify({'state':'1'})
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg':ae})

def create_employee(employee_info):
    if not verify_employeename(employee_info['employee_id']):
        return jsonify({'stste':'0','error_msg':'Illegal employee id'})
    elif not (employee_info['password'] == employee_info['confirm_password']):
        return jsonify({'state':'0','error_msg':'Tow passwords are different'})
    elif not verify_password(employee_info['password']):
        return jsonify({'stste':'0','error_msg':'Illegal password'})
    else:
        try:
            db_adi_opr.create_employee(employee_info['employee_id'], employee_info['password'])
            return jsonify({'stste':'1'})
        except AssertionError as ae:
            return jsonify({'stste':'0','error_msg':ae})

def delete_employee(employee_id):
    try:
        db_adi_opr.delete_employee(employee_id)
        return jsonify({'stste':'1'})
    except AssertionError as ae:
        return jsonify({'stste':'0','error_msg':ae})

def update_employee_password(update_employee_info):
    if not (update_employee_info['password'] == update_employee_info['confirm_password']):
        return jsonify({'state':'0','error_msg':'Tow passwords are different'})
    elif not verify_password(update_employee_info['password']):
        return jsonify({'stste':'0','error_msg':'Illegal password'})
    else:
        try:
            db_adi_opr.update_employee_password(update_employee_info['employee_id'], update_employee_info['password'])
            return jsonify({'stste':'1'})
        except AssertionError as ae:
            return jsonify({'stste':'0','error_msg':ae})

def create_user(create_user_info):
    return user.register(create_user_info)

def delete_user(username):
    try:
        db_usr_opr.delete_user(username)
        return jsonify({'stste':'1'})
    except AssertionError as ae:
        return jsonify({'stste':'0','error_msg':ae})

def update_user_password(update_user_info):
    return user.update_password(update_user_info['username'],update_user_info['password'],update_user_info['confirm_password'])