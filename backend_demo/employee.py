from re_verification import *
from flask import jsonify
import db_operation.employee_operate as db_emp_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr

def login(employeeid,password):
    try:
        return_message = db_emp_opr.login(employeeid, password)
        success_message = "Login successfully"
        if return_message == success_message:
            return_value = {'state': '2'}
            return jsonify(return_value)
    except AssertionError as ae:
        if ae == 'No such id':
            return_value = {'state': '-1', 'error_msg': 'No such employee'}
            return jsonify(return_value)
        elif ae == 'Wrong password':
            return_value = {'state': '0', 'error_msg': 'Password is not correct'}
            return jsonify(return_value)

def update_password(employeeid,new_password,confirm_password):
    if not verify_password(new_password):
        return "新密码不合法"
    elif not (new_password == confirm_password):
        return "两次输入的密码不一样"
    else:
        try:
            return db_emp_opr.update_password(employeeid,new_password)
        except AssertionError as ae:
            return ae

def list_all_insurance():
    return db_ins_opr.all()

def list_all_claim():
    return db_cla_opr.all()

def address_claim(claim_id,state):
    try:
        return db_cla_opr.change_staue(claim_id,state)
    except AssertionError as ae:
        return "失败,reason:"+ae