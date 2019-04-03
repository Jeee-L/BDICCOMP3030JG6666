from www.model.component.database_basic.whats_your_name import Employee,db


def search_id(id):
    return not not Employee.query.filter_by(id = id).first()

def login(id, password):
    if not search_id(id):
        return 'No such id'
    elif not Employee.query.filter_by(id = id, password=password).first():
        return 'Password wrong'
    else:
        return 'Successful'

def create(id, password):
    if not login(id):
        db.session.add(Employee(id = id, password = password))
        db.session.commit()
        return 'Successful'
    else:
        return 'Already exist'

def update_password(id, new_password):
    if search_id(id):
        if login(id, new_password) == 'Successful':
            return 'Same password'
        else:
            Employee.query.filter_by(id=id).first().password = new_password
            return 'successful'
    else:
        return 'No such Employee'


def delete(id):
    if search_id(id):
        db.session.delete(Employee.query.filter_by(id=id).first())
        db.session.commit()
        return 'successful'
    else:
        return 'No such employee'