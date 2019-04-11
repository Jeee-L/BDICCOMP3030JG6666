from re_verification import *
from flask import jsonify
import db_operation.users_operate as db_usr_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr
import db_operation.administrator_operate as db_adi_opr

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

def update_password(administratorid,new_password,confirm_password):
    if not verify_password(new_password):
        return "新密码不合法"
    elif not (new_password == confirm_password):
        return "两次输入的密码不一样"
    else:
        try:
            return db_adi_opr.update_password(administratorid,new_password)
        except AssertionError as ae:
            return ae

def create_new_administrator(id,password,confirm_password):
    if not verify_password(password):
        return "新密码不合法"
    elif not (password == confirm_password):
        return "两次输入的密码不一样"
    elif not verify_administrator_name(id):
        return "新管理员名不合法"
    else:
        try:
            return db_adi_opr.create(id,password)
        except AssertionError as ae:
            return "创建失败,reason:"+ae

def delete_administrator(current_id,delete_id):
    if current_id == delete_id:
        return "不能删除自己"
    elif delete_id == 'a@root': #TODO 管理员名字？
        return "不能删除保留管理员"
    else:
        try:
            return db_adi_opr.delete(delete_id)
        except AssertionError as ae:
            return "删除失败,reason:"+ae

def create_employee(employee_id,password,confirm_password):
    if not verify_employeename(employee_id):
        return "新员工名不合法"
    elif not (password == confirm_password):
        return "两次输入密码不一致"
    elif not verify_password(password):
        return "新员工密码不合法"
    else:
        try:
            return db_adi_opr.create_employee(employee_id,password)
        except AssertionError as ae:
            return "创建员工失败,reason:"+ae

def delete_employee(employee_id):
    try:
        return db_adi_opr.delete_employee(employee_id)
    except AssertionError as ae:
        return "删除员工失败,reason:"+ae

def update_employee_password(employee_id,password,confirm_password):
    if not (password == confirm_password):
        return "两次输入密码不一致"
    elif not verify_password(password):
        return "新员工密码不合法"
    else:
        try:
            return db_adi_opr.update_employee_password(employee_id, password)
        except AssertionError as ae:
            return "更改员工密码失败,reason:" + ae

def delete_user(username):
    try:
        return db_usr_opr.delete_user(username)
    except AssertionError as ae:
        return "删除用户失败,reason:"+ae