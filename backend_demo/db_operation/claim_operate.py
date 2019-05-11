from db_operation.database_basic.whats_your_name import Claim,db
from db_operation.order import search_order


def add_claim(dict):
    '''
    增加
    :param dict:
    :return:
    '''
    assert (search_order(id) is not None), 'No such order id'
    db.session.add(Claim(order_id=dict['order_id'],lost_time=dict['lost_time'],lost_place=dict['lost_place'], employee_id=dict['employee_id'], reason=dict['reason'],remark=dict['remark'], state=dict['state']))
    db.session.commit()
    return 'Create Claim successfully'

def search_claim_use_order_id(id):
    '''
    查找
    :param id:
    :return:
    '''
    return Claim.query.filter_by(order_id = id).all()

def __search_claim(id):
    '''
    查找claim
    :param id:
    :return:
    '''
    return Claim.query.filter_by(id=id).first()

def cancel_claim(id):
    '''

    :param id:
    :return:
    '''
    claim = __search_claim(id)
    assert(claim is not None), 'No such Claim'
    claim.state = -2
    db.session.commit()
    return 'cancel Successfully'

def change_state(id, state,employee_id):
    '''

    :param id:
    :param state:
    :return:
    '''
    claim = __search_claim(id)
    assert claim is not None,'No such Claim'
    claim.state = state
    claim.employee_id = employee_id
    db.session.commit()
    return 'Change successfully'

def update_state(id, state):
    '''

    :param id:
    :param state:
    :return:
    '''
    claim = __search_claim(id)
    assert claim is not None, 'No such Claim'
    claim.state = state
    db.session.commit()
    return 'Change successfully'


def all():
    '''

    :return:
    '''
    return Claim.query.all()




if __name__ == '__main__':
    print(all())