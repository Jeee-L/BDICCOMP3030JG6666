from db_operation.database_basic.whats_your_name import Project,db
def update_attribute(attribute_name, new_attribute):
    '''

    :param attribute_name: 旧的属性名称， str
    :param new_attribute: 新的属性
    :return: list[原来的值， 新的值]
    '''
    res = []




    return res

def insert_project(dict):
    p = Project(product_id=dict['product_id'], project_id=dict['project_id'], coverage=dict['coverage'], amount_of_each_shipment_insured=dict['amount_of_each_shipment_insured'], premium=dict['premium'])
    db.session.add(p)
    db.session.commit()
    return p

