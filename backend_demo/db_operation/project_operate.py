from backend_demo.db_operation.database_basic.whats_your_name import Project,db


def insert_project(dict):
    p = Project(product_id=dict['product_id'], project_id=dict['project_id'], coverage=dict['coverage'], amount_of_each_shipment_insured=dict['amount_of_each_shipment_insured'], premium=dict['premium'])
    db.session.add(p)
    db.session.commit()
    return p

