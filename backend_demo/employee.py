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
    all_insurance = db_ins_opr.all()
    return_list = []
    if all_insurance is []:
        return ""
    else:
        for insurance in all_insurance:
            insurance_dict = {}
            insurance_dict['username'] = insurance.username
            insurance_dict['id'] = insurance.id
            insurance_dict['project_id'] = insurance.project_id
            insurance_dict['product_id'] = insurance.product_id
            insurance_dict['amount_of_money'] = insurance.amount_of_money
            insurance_dict['compensated_amount '] = insurance.compensated_amount
            insurance_dict['status'] = insurance.status
            insurance_dict['date'] = insurance.date
            insurance_dict['remark'] = insurance.remark
            return_list.append(insurance_dict)
        return jsonify(return_list)

def list_all_claim():
    all_claim = db_cla_opr.all()
    return_list = []
    if all_claim is []:
        return ""
    else:
        for claim in all_claim:
            claim_dict = {}
            # claim 中没有username，先查insurance再通过insurance查username，待测试
            claim_dict['username'] = (db_ins_opr.__search_insurance(claim.insurance_id)).username
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
        return jsonify(return_list)

def address_claim(address_info):
    try:
        db_cla_opr.change_staue(address_info['claim_id'], address_info['state'])
        return jsonify({'state':'1'})
    except AssertionError as ae:
        return jsonify({'state':'0','error_msg':ae})