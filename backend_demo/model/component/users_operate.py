from model.component.database_basic.whats_your_name import Users,db


def search_username(username):
    '参数:username， return: 是否取得'
    return Users.query.filter_by(name=username).first()

def password_is_right(username, password):
    '参数:username, password'
    user = search_username(username)
    return user.check_password_hash(password)


def insert_user(list):
    '参数:list name,password,phone_num,passport_num,email, return boolean'
    if not search_username(list[0]):
        db.session.add(Users(name=list[0],password=list[1],phone_num=list[2],passport_num=list[3],email=list[4]))
        db.session.commit()
        return 'Create successfully'
    return 'Username already exist'


def update_username(username, new_name):
    if not not search_username(username):
        if not search_username(new_name):
            user = Users.query.filter_by(name=username).first()
            user.name = new_name
            db.session.commit()
            return True
    return False


def update_password(username, new_password):
    if not search_username(username):
        return 'No such user'
    user = search_username(username)
    if user.check_password_hash(new_password):
        return False
    user.password = new_password
    return True

def update_phone_num(username,new_phone_num):
    if not search_username(username):
        return 'No such user'
    user = search_username(username)
    if user.phone_num == new_phone_num:
        return False
    user.phone_num = new_phone_num
    return True

def update_passport_num(username,new_passport_num):
    if not search_username(username):
        return 'No such user'
    user = search_username(username)
    if new_passport_num == user.passport_num:
        return False
    user.password = new_passport_num
    return True

def update_email(username, new_email):
    if not search_username(username):
        return 'No such user'
    user = search_username(username)
    if new_email == user.email:
        return 'Same email'
    user.password = new_email
    return 'Update email successfully'

def delete_user(username):
    if not search_username(username):
        return 'Can\' find user'
    db.session.delete(search_username(username))
    db.session.commit()
    return 'Delete successfully'

if __name__ == '__main__':
    insert_user(['1cfabds','1afsdfff',1213334,1233413,'133f23@1163.com'])
    print(search_username('1cfabds').password_hash)
    print(password_is_right('1cfabds', '1afsdfff'))