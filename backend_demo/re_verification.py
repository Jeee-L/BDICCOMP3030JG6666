import re

def verify_username(username):
    valid_name = r'^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$'
    if re.match(valid_name,username):
        return True
    else:
        return False

def verify_password(password):
    valid_password = r'^[_!?,.*#a-zA-Z0-9]{6,20}$'
    if re.match(valid_password,password):
        return True
    else:
        return False

def verify_email(email):
    valid_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    if re.match(valid_email,email):
        return True
    else:
        return False

def verify_phone_number(phonenumber):
    valid_phone = r'^1[34578]\d{9}$|^\d{8,9}$'
    if re.match(valid_phone, phonenumber):
        return True
    else:
        return False

def verify_employeename(employeename):
    valid_employeename = r'^e@[_a-zA-Z0-9\u4E00-\u9FA5]{1,10}$'
    if re.match(valid_employeename,employeename):
        return True
    else:
        return False

def verify_administrator_name(administrator_name):
    valid_administrator_name = r'^a@[_a-zA-Z0-9\u4E00-\u9FA5]{1,10}$'
    if re.match(valid_administrator_name, administrator_name):
        return True
    else:
        return False

def verify_passport(passport):
    # 因私普通护照号码格式有:14/15+7位数,G+8位数；
    # 因公普通的是:P.+7位数；公务的是：S.+7位数 或者 S+8位数,以D开头的是外交护照.D=diplomatic
    # H:香港特区护照和香港公民所持回乡卡H开头,后接10位数字
    # M:澳门特区护照和澳门公民所持回乡卡M开头,后接10位数字
    valid_passport = r'^(1[45]|P|E[A-Z])\d{7}$|^[GDE](\d{8})$|^S\d{7,8}$|^[HM]\d{10}$'
    if re.match(valid_passport, passport):
        return True
    else:
        return False

def verify_flight_number(flight_num):
    # 数字加大写字母开头，或者两个/三个大写字母，后面是2个到4个数字
    valid_flight_num = r'^[\dA-Z][A-Z]{1,2}\d{2,4}$'
    if re.match(valid_flight_num, flight_num):
        return True
    else:
        return False