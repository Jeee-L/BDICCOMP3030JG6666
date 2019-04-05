from www.model.component.users_operate import search_username
from www.model.component.database_basic.whats_your_name import Insurance,db
import datetime

def __search_insurance(id):
    return Insurance.query.filter_by(id = id).first()

def add_insurance(dict):
    'id,name[0],product_id[1],amount_of_money[2],status,flight_number[3]'
    'status are the one of set (Creating, using, out_date)'
    assert (search_username(dict['name']) is not None), "No such Insurance"
    f = Insurance(name=dict['name'], product_id=dict['product_id'], amount_of_money=dict['amount_of_money'], flight_number=dict['flight_number'], status=dict['status'], date =datetime.datetime.now() )
    db.session.add(f)
    db.session.commit()
    return f.id