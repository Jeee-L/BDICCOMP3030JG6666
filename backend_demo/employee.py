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
            return jsonify({'state': '2'})
    except AssertionError as ae:
        if ae == 'No such id':
            return_value = {'state': '-1', 'error_msg': 'No such employee'}
            return jsonify(return_value)
        elif ae == 'Wrong password':
            return_value = {'state': '0', 'error_msg': 'Password is not correct'}
            return jsonify(return_value)

def update_password(employee_update_info):
    if not verify_password(employee_update_info['new_password']):
        return jsonify({'state':'0','error_msg':'Illegal password'})
    elif not (employee_update_info['new_password'] == employee_update_info['confirm_password']):
        return jsonify({'state':'0','error_msg':'Tow passwords are different'})
    else:
        try:
            db_emp_opr.update_password(employee_update_info['employeeid'], employee_update_info['new_password'])
            return jsonify({'state':'1'})
        except AssertionError as ae:
            return jsonify({'state':'0','error_msg':ae})

def list_all_insurance():
    all_insurance = {'orders':db_ins_opr.all()}
    return jsonify(all_insurance)

def list_all_claim():
    all_claim = {'claims':db_cla_opr.all()}
    return jsonify(all_claim)

def address_claim(address_info):
    try:
        db_cla_opr.change_staue(address_info['claim_id'], address_info['state'])
        return jsonify({'state':'1'})
    except AssertionError as ae:
        return jsonify({'state':'0','error_msg':ae})