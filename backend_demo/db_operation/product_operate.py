from db_operation.database_basic.whats_your_name import Product,db
def update_attribute(attribute_name, new_attribute):
    '''

    :param attribute_name: 旧的属性名称， str
    :param new_attribute: 新的属性
    :return: list[原来的值， 新的值]
    '''
    res = []




    return res

def insert_product(dict):
    p = Product(product_id=dict['product_id'], product_information=dict['product_information'])
    db.session.add(p)
    db.session.commit()
    return p



