from www.model.component.database_basic.whats_your_name import Administrator,db
import www.model.component.employee_operate as emp


def search_id(id):
    return Administrator.query.filter_by(id = id).first()

def login(id, password):
    admin = search_id(id)
    assert(search_id(id) is not None),'No such id'
    assert(admin.check_password_hash(password)), 'Password wrong'
    return 'Login successfully'


def create(id, password):
    assert(search_id(id) is None),'Administrator already exist'
    db.session.add(Administrator(id = id, password = password))
    db.session.commit()
    return 'Create successfully'

def update_password(id, new_password):
    admin = search_id(id)
    assert (admin is not None), 'No such administrator'
    assert (not admin.check_password_hash(new_password)),'Same password'
    admin.password = new_password
    return 'Update successfully'



def delete(id):
    '''

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

    :param id:
    :return:
    '''
    return emp.delete(id)

def update_employee_password(id, password):
    '''

    :param id:
    :param password:
    :return:
    '''
    return emp.update_password(id,password)

def create_employee(id, password):
    '''

    :param id:
    :param password:
    :return:
    '''
    return emp.create(id, password)

def search_employee(id):
    '''

    :param id:
    :return:
    '''
    return emp.search_id(id)