from db_operation.users_operate import *
from db_operation.insurance_operate import *
from db_operation.product_operate import insert_product
from db_operation.project_operate import *
from db_operation.test.read import read
from db_operation.database_basic.database_operate import recreate_table


def test_for_insert():

    s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\user.csv')
    for item in s:
        insert_user(item)
    insert_product({'product_id':1, 'product_information':''})
    insert_project({'product_id':1, 'project_id':1, 'coverage':1, 'amount_of_each_shipment_insured':1, 'premium':1})

    s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\insurances.csv')
    for item in s:
        add_insurance(item)
    print('insert successfully')

def test_for_update():
    print('update successfully')

def test_for_delete():
    print('delete successfully')

def test_for_search():
    print('search successfully')


if __name__=='__main__':
    recreate_table()
    test_for_insert()
    test_for_search()
    test_for_update()
    test_for_delete()
    test_for_search()
