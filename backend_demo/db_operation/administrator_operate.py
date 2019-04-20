from backend_demo.db_operation.database_basic.whats_your_name import Administrator,db
import backend_demo.db_operation.employee_operate as emp


def search_id(id):
    return Administrator.query.filter_by(id = id).first()

def login(id, password):
    '''
    登陆管理员
    :param id: administrator id
    :param password: administrator 密码
    :return:
    '''
    admin = search_id(id)
    assert(search_id(id) is not None),'No such id'
    assert(admin.check_password_hash(password)), 'Password wrong'
    return 'Login successfully'


def create(id, password):
    '''
    创建管理员
    :param id:
    :param password:
    :return:
    '''
    assert(search_id(id) is None),'Administrator already exist'
    db.session.add(Administrator(id = id, password = password))
    db.session.commit()
    return 'Create successfully'

def update_password(id, new_password):
    '''
    修改管理员密码
    :param id:
    :param new_password:
    :return:
    '''
    admin = search_id(id)
    assert (admin is not None), 'No such administrator'
    assert (not admin.check_password_hash(new_password)),'Same password'
    admin.password = new_password
    return 'Update successfully'



def delete(id):
    '''
    删除管理员 通过管理员id
    :param id:
    :return:
    '''
    admin = search_id(id)
    assert(admin is not None),'No such administrator'
    db.session.delete(admin)
    db.session.commit()
    return 'Delete successfully'


def delete_employee(id):
    '''
    删除员工 通过员工id
    :param id:
    :return:
    '''
    return emp.delete(id)

def update_employee_password(id, password):
    '''
    通过id修改员工密码
    :param id:
    :param password:
    :return:
    '''
    return emp.update_password(id,password)

def create_employee(id, password):
    '''
    创建员工
    :param id:
    :param password:
    :return:
    '''
    return emp.create(id, password)

def search_employee(id):
    '''
    查找员工
    :param id:
    :return:
    '''
    return emp.search_id(id)

