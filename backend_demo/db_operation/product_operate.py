from db_operation.database_basic.whats_your_name import Product,db

def search_product(product_id):
    return Product.query.filter_by(product_id=product_id).first()

def insert_product(dict):

    p = Product(product_id=dict['product_id'], product_information=dict['product_information'])
    if search_product(dict['product_id']) is None:
        db.session.add(p)
        db.session.commit()
    return p




