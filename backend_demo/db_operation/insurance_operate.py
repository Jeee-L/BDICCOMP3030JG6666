from backend_demo.db_operation.users_operate import search_username
from backend_demo.db_operation.database_basic.whats_your_name import Insurance,db
import datetime


def __search_insurance(id):
    '''

    :param id:
    :return:
    '''
    return Insurance.query.filter_by(id = id).first()

def add_insurance(dict):
    '''

    :param dict: username[0],product_id[1],project_id[2], amount_of_money[3],status,flight_number[4],status are the one of set (Creating, using, out_date)
    :return: id
    '''
    assert (search_username(dict['username']) is not None), "No such User"
    f = Insurance(username=dict['username'], product_id=dict['product_id'], project_id=dict['project_id'], amount_of_money=dict['amount_of_money'],  status=dict['status'], date =datetime.datetime.now() )
    db.session.add(f)
    db.session.commit()
    return f.id

def change_state(id, state):
    '''

    :param id: 保险id int
    :param state: 保险状态 int
    :return:
    '''
    ins = __search_insurance(id)

    assert ins is not None,'No such Insurance'
    ins.status = state
    return 'Change successfully'

def all():
    '''

    :return: list
    '''
    return Insurance.query.all()

def search_claim(ins):
    '''

    :param ins:
    :return:
    '''
    return ins.claim_id.first()

def user_all_insurance(username):
    '''

    :param username:
    :return:
    '''
    return Insurance.query.filter_by(username = username).all()





