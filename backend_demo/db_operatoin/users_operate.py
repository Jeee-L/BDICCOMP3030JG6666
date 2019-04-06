from www.model.component.database_basic.whats_your_name import Users,db


def search_username(username):
    '参数:username， 用户对象，否则None'
    return Users.query.filter_by(name=username).first()

def password_is_right(username, password):
    '参数:username, password'
    user = search_username(username)
    return user.check_password_hash(password)

def insert_user(dict):
    '参数:dict name,password,phone_num,passport_num,email, return boolean'
    user = search_username(dict['name'])
    assert (user is None), "Username already exist"
    db.session.add(Users(name=dict['name'],password=dict['password'],phone_num=dict['phone_num'],passport_num=dict['passport_num'],email=dict['email'], profile=dict['profile']))
    db.session.commit()
    return 'Create successfully'

def update_profile(username, new_profile):
    user = search_username(username)
    assert user is not None, 'No such user'
    user.profile = new_profile
    db.session.commit()
    return "Update successfully"

def update_username(username, new_name):
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (not search_username(new_name)), 'This name already exist'
    user.name = new_name
    db.session.commit()
    return "Update successfully"

def update_password(username, new_password):
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (not user.check_password_hash(new_password)),'Same password'
    user.password = new_password
    return "Update successfully"

def update_phone_num(username,new_phone_num):
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.phone_num is not new_phone_num), 'Same phone num'
    user.phone_num = new_phone_num
    return "Update successfully"

def update_passport_num(username,new_passport_num):
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.passport_num is not new_passport_num), 'Same passport_num'
    user.password = new_passport_num
    return "Update successfully"

def update_email(username, new_email):
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.email is not new_email), 'Same email'
    user.password = new_email
    return 'Update email successfully'

def delete_user(username):
    user = search_username(username)
    assert (user is not None), "No such user"
    db.session.delete(user)
    db.session.commit()
    return 'Delete successfully'

if __name__ == '__main__':
    # insert_user(['1cfabds','1afsdfff',1213334,1233413,'133f23@1163.com'])
    print(search_username('1cfabdss'))
    print(password_is_right('1cfabds', '1afsdfff'))