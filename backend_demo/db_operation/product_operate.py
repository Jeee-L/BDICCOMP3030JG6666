from db_operation.database_basic.whats_your_name import Product,db


def insert_product(dict):
    p = Product(product_id=dict['product_id'], product_information=dict['product_information'])
    db.session.add(p)
    db.session.commit()
    return p




