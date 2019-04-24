import datetime

from backend_demo.db_operation.insurance_operate import __search_insurance
from backend_demo.db_operation.database_basic.whats_your_name import Order,db
from backend_demo.db_operation.users_operate import search_username

def search_order(obj):
    '''

    :param obj:
    :return: 如果是id 返回一个， 如果是姓名 返回一串
    '''

    if type(obj) == int:
        return Order.query.filter_by(order_id = obj).first()
    else:
        return Order.query.filter_by(username=obj).all()

def change_state(id, state):
    '''

    :param id: order id int
    :param state: order状态 int
    :return:
    '''
    ord = search_order(id)
    ord.status = state
    return 'Change successfully'


def add_order(dict):
    '''
state,insurance_id,username,flight_number,luggage_image_outside,luggage_image_inside,luggage_height,luggage_width,claim_id
    :param dict:dict for order status are the one of set (Creating, using, out_date)
    :return: id
    '''
    if search_username(dict['username']) is None:
        print( "No such User {}".format(dict['username']))
    f = Order(username=dict['username'], flight_number =  dict['flight_number'], luggage_image_inside=dict['luggage_image_inside'],luggage_image_outside=dict['luggage_image_outside'], luggage_width=dict['luggage_width'],
              luggage_height=dict['luggage_height'],state=dict['state'], date =datetime.datetime.now() ,remark=dict['remark'])
    db.session.add(f)
    db.session.commit()
    return f.order_id


def delete_order(id):
    '''

    :param id:
    :return:
    '''
    db.session.delete(search_order(id))
    db.session.commit()

