from backend_demo.db_operation.users_operate import *
from backend_demo.db_operation.insurance_operate import *
from backend_demo.db_operation.product_operate import insert_product
from backend_demo.db_operation.project_operate import *
from backend_demo.db_operation.test.read import read


def test():
    s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\user.csv')
    for item in s:
        insert_user(item)
    insert_product({'product_id':1, 'product_information':''})
    insert_project({'product_id':1, 'project_id':1, 'coverage':'', 'amount_of_each_shipment_insured':1, 'premium':1})

    s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\insurances.csv')
    for item in s:
        add_insurance(item)

if __name__=='__main__':
    test()