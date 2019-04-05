from model.component.users_operate import search_username
from model.component.database_basic.whats_your_name import Insurance,db
import datetime

def __search_insurance(id):
    return Insurance.query.filter_by(id = id).first()

def add_insurance(list):
    'id,name[0],product_id[1],amount_of_money[2],status,flight_number[3]'
    'status are the one of set (Creating, using, out_date)'
    if not search_username(list[0]):
        return 'No such user'
    f = Insurance(name=list[0], product_id=list[1], amount_of_money=list[2], flight_number=list[3], status='Creating', date =datetime.datetime.now() )

    db.session.add(f)
    db.session.commit()
    return f.id