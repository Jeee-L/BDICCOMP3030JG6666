import datetime

from backend_demo.db_operation.insurance_operate import __search_insurance
from backend_demo.db_operation.database_basic.whats_your_name import Order,db,Select_img
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

def all():
    return Order.query.all()


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

    :param dict:dict for order status are the one of set (Creating, using, out_date)
    :return: id
    '''
    assert (search_username(dict['username']) is not None), "No such User"
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

def select_img(id):
    return Select_img.query.filter_by(order_id = id).all()

def add_img(dict):
    db.session.add(Select_img(order_id = dict['order_id'], imgUrl = dict['imgUrl'], name = dict['name'] , remark = dict['remark'] , price = dict['price']))
