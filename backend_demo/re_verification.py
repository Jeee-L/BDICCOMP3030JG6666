import re

def verify_username(username):
    valid_name = r'^[_a-zA-Z0-9\u4E00-\u9FA5]{1,10}$'
    if re.match(valid_name,username):
        return True
    else:
        return False

def verify_password(password):
    valid_password = r'^[_!?,.*#a-zA-Z0-9]{1,20}$'
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
    # TODO phone number
    pass

def verify_employeename(employeename):
    valid_employeename = r'^[e|E]@[_a-zA-Z0-9\u4E00-\u9FA5]{1,10}$'
    if re.match(valid_employeename,employeename):
        return True
    else:
        return False

def verify_root(rootname):
    # TODO 是否可以修改root这个名字？
    valid_root = r'[e|E]@[r|R]oot'
    if re.match(valid_root, rootname):
        return True
    else:
        return False