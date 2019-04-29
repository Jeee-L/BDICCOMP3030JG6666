from db_operation.database_basic.whats_your_name import Project,db


def insert_project(dict):
    p = Project(product_id=dict['product_id'], project_id=dict['project_id'], coverage=dict['max_total'], amount_of_each_shipment_insured=dict['max_per_time'], premium=dict['price'])
    db.session.add(p)
    db.session.commit()
    return p

def search_project(product_id, project_id):
    return Project.query.filter_by(product_id=product_id, project_id = project_id).first().id