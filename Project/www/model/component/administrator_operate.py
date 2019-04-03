from www.model.component.database_basic.whats_your_name import Administrator,db
import www.model.component.employee_operate as emp


def search_id(id):
    return not not Administrator.query.filter_by(id = id).first()

def login(id, password):
    if not search_id(id):
        return 'No such id'
    elif not Administrator.query.filter_by(id = id, password=password).first():
        return 'Password wrong'
    else:
        return 'Successful'

def create(id, password):
    if not login(id):
        db.session.add(Administrator(id = id, password = password))
        db.session.commit()
        return 'Successful'
    else:
        return 'Already exist'

def update_password(id, new_password):
    if search_id(id):
        if login(id, new_password) == 'Successful':
            return 'Same password'
        else:
            Administrator.query.filter_by(id=id).first().password = new_password
            return 'successful'
    else:
        return 'No such administrator'


def delete(id):
    if search_id(id):
        db.session.delete(Administrator.query.filter_by(id=id).first())
        db.session.commit()
        return 'successful'
    else:
        return 'No such administrato'

def delete_employee(id):
    return emp.delete(id)

def update_employee_password(id, password):
    return emp.update_password(id,password)

def create_employee(id, password):
    return emp.create(id, password)

def search_employee(id):
    return emp.search_id(id)