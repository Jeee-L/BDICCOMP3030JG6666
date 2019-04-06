from www.model.component.users_operate import search_username
from www.model.component.database_basic.whats_your_name import Insurance,db
import datetime

def __search_insurance(id):
    return Insurance.query.filter_by(id = id).first()

def add_insurance(dict):
    'id,name[0],product_id[1],amount_of_money[2],status,flight_number[3]'
    'status are the one of set (Creating, using, out_date)'
    assert (search_username(dict['name']) is not None), "No such User"
    f = Insurance(name=dict['username'], product_id=dict['product_id'], amount_of_money=dict['amount_of_money'], flight_number=dict['flight_number'], status=dict['status'], date =datetime.datetime.now(),pic=dict['image'] )
    db.session.add(f)
    db.session.commit()
    return f.id

def change_staue(id, state):
    ins = __search_insurance(id)
    assert ins is not None,'No such Insurance'
    ins.status = state
    return 'Change successfully'

if __name__ == '__main__':
    add_insurance({'name':'1cfabds','product_id':123,'amount_of_money':123, 'flight_number':123,'status':'123', 'pic':223})