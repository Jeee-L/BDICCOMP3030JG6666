from re_verification import *
from flask import jsonify
import db_operation.employee_operate as db_emp_opr
import db_operation.insurance_operate as db_ins_opr
import db_operation.claim_operate as db_cla_opr
import db_operation.order as db_ord_opr

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
            insurance_dict['state'] = insurance.state
            insurance_dict['date'] = insurance.date
            insurance_dict['remark'] = insurance.remark
            return_list.append(insurance_dict)
        return return_list

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
            claim_dict['insurance_order_id'] = claim.order_id
            claim_dict['id'] = claim.id
            claim_dict['employee_id'] = claim.employee_id
            claim_dict['reason'] = claim.reason
            claim_dict['state'] = claim.state
            claim_dict['lost_time'] = claim.lost_time
            claim_dict['lost_place'] = claim.lost_place
            claim_dict['date'] = claim.time
            claim_dict['remark'] = claim.remark
            return_list.append(claim_dict)
        return return_list

def list_all_insurance_order():
    all_insurance_order = db_ord_opr.all()
    return_list = []
    if all_insurance_order is []:
        return ""
    else:
        for insurance_order in all_insurance_order:
            insurance_dict = {}
            insurance_dict['id'] = insurance_order.id
            insurance_dict['state'] = insurance_order.state
            insurance_dict['username'] = insurance_order.username
            insurance_dict['insurance_id'] = insurance_order.insurance_id
            insurance_dict['flight_number'] = insurance_order.flight_number
            insurance_dict['luggage_image_outside'] = insurance_order.luggage_image_outside
            insurance_dict['luggage_image_inside'] = insurance_order.luggage_image_inside
            insurance_dict['luggage_height'] = insurance_order.luggage_height
            insurance_dict['luggage_width'] = insurance_order.luggage_width
            insurance_dict['date'] = insurance_order.date
            insurance_dict['claim_id'] = insurance_order.claim_id
            insurance_dict['remark'] = insurance_order.remark
            return_list.append(insurance_dict)
        return return_list

def insurance_order_detail(insurance_order_id):
    insurance_order = db_ord_opr.search_order(insurance_order_id)
    if insurance_order is None:
        return jsonify({'state':'-1','error_msg':'No such insurance order'})
    else:
        insurance_order_dict = {}
        insurance_order_dict['order_id'] = insurance_order.id
        insurance_order_dict['state'] = insurance_order.state
        insurance_order_dict['username'] = insurance_order.username
        insurance_order_dict['insurance_id'] = insurance_order.insurance_id
        insurance_order_dict['flight_number'] = insurance_order.flight_number
        insurance_order_dict['luggage_image_outside'] = insurance_order.luggage_image_outside
        insurance_order_dict['luggage_image_inside'] = insurance_order.luggage_image_inside
        insurance_order_dict['luggage_height'] = insurance_order.luggage_height
        insurance_order_dict['luggage_width'] = insurance_order.luggage_width
        insurance_order_dict['date'] = insurance_order.date
        insurance_order_dict['claim_id'] = insurance_order.claim_id
        insurance_order_dict['remark'] = insurance_order.remark
        insurance_order_dict['sumPrice'] = insurance_order.sumPrice
        select_img_list = db_ord_opr.select_img(insurance_order_id)
        select_img_return_list = []
        for select_img in select_img_list:
            select_img_dict = {}
            select_img_dict['imgUrl'] = select_img.imgUrl
            select_img_dict['name'] = select_img.name
            select_img_dict['price'] = select_img.price
            select_img_dict['remark'] = select_img.remark
            select_img_return_list.append(select_img_dict)
        insurance_order_dict['select_img'] = select_img_return_list
    return jsonify(insurance_order_dict)

def address_claim(address_info):
    try:
        db_cla_opr.change_state(address_info['claim_id'], address_info['state'], address_info['employee_id'])
        return jsonify({'state':'1'})
    except AssertionError as ae:
        return jsonify({'state':'0','error_msg':ae})

def all_employees():
    employee_list = db_emp_opr.all()
    if employee_list is []:
        return ""
    else:
        return_list = []
        for employee in employee_list:
            employee_dict = {}
            employee_dict['employee_id'] = employee.id
            return_list.append(employee_dict)
        return return_list