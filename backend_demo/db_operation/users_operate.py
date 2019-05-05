from db_operation.database_basic.whats_your_name import Users,db,Claim




def search_username(username):
    '''

    :param username:
    :return:
    '''
    return Users.query.filter_by(username=username).first()

def password_is_right(username, password):
    '''

    :param username:
    :param password:
    :return:
    '''
    user = search_username(username)
    return user.check_password_hash(password)

def insert_user(dict):
    '''

    :param dict:
    :return:
    '''
    user = search_username(dict['username'])
    assert (user is None), "Username already exist"
    db.session.add(Users(username=dict['username'], password=dict['password'],phone_num=dict['phone_num'],email=dict['email']))
    db.session.commit()
    return 'Create successfully'

def get_insurance(username):
    '''

    :param username:
    :return:
    '''
    user = search_username(username)
    assert (user is None), "Username already exist"
    return user.insurance_id.all()

def get_order(username):
    user=search_username(username)
    return user.order_id.all()

def get_claim(username):
    '''

    :param username:
    :return:
    '''
    user = search_username(username)
    assert (user is None), "Username already exist"
    inss = user.order_id.all()
    res = []
    if inss is not []:
        for ins in inss:
            res.append(Claim.query.filter_by(insurance_id = ins.insurance_id).first())
    return res


def update_profile(username, new_profile):
    '''

    :param username:
    :param new_profile:
    :return:
    '''
    user = search_username(username)
    assert user is None, 'No such user'
    user.profile = new_profile
    db.session.commit()
    return "Update successfully"

def update_username(username, new_name):
    '''

    :param username:
    :param new_name:
    :return:
    '''
    user = search_username(username)
    assert (user is None), "No such user"
    assert (not search_username(new_name)), 'This name already exist'
    user.username = new_name
    db.session.commit()
    return "Update username successfully"

def update_first_name(username, first_name):
    '''

    :param username:
    :param first_name:
    :return:
    '''
    user = search_username(username)
    assert (user is None), "No such user"
    user.first_name = first_name
    db.session.commit()
    return "Update first name successfully"

def update_last_name(username, last_name):
    '''

    :param username:
    :param last_name:
    :return:
    '''
    user = search_username(username)
    assert (user is None), "No such user"
    user.last_name = last_name
    db.session.commit()
    return "Update last name successfully"

def update_birthday(username, birthday):
    '''

    :param username:
    :param birthday:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    user.birthday = birthday
    db.session.commit()
    return "Update birthday successfully"

def update_address(username, address):
    '''

    :param username:
    :param address:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    user.address = address
    db.session.commit()
    return "Update address successfully"

def update_password(username, new_password):
    '''

    :param username:
    :param new_password:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (not user.check_password_hash(new_password)),'Same password'
    user.password = new_password
    db.session.commit()
    return "Update password successfully"

def update_phone_num(username,new_phone_num):
    '''

    :param username:
    :param new_phone_num:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.phone_num is not new_phone_num), 'Same phone num'
    user.phone_num = new_phone_num
    db.session.commit()
    return "Update phone number successfully"

def update_passport_num(username,new_passport_num):
    '''

    :param username:
    :param new_passport_num:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.passport_num is not new_passport_num), 'Same passport_num'
    user.passport_num = new_passport_num
    db.session.commit()
    return "Update passport number successfully"

def update_email(username, new_email):
    '''

    :param username:
    :param new_email:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    assert (user.email is not new_email), 'Same email'
    user.email = new_email
    db.session.commit()
    return 'Update email successfully'

def delete_user(username):
    '''

    :param username:
    :return:
    '''
    user = search_username(username)
    assert (user is not None), "No such user"
    db.session.delete(user)
    db.session.commit()
    return 'Delete successfully'


def all():
    return Users.query.all()



