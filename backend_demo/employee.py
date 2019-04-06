from re_verification import *
import db_operatoin.employee_operate as db_emp_opr
import db_operatoin.insurance_operate as db_ins_opr
import db_operatoin.claim_operate as db_cla_opr

def login(employeeid,password):
    if not verify_password(password):
        return "密码不合法"
    elif not verify_employeename(employeeid):
        return "员工名不合法"
    else:
        try:
            return db_emp_opr.login(employeeid,password)
        except AssertionError as ae:
            return "登陆失败,reason:"+ae

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