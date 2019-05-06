from db_operation.users_operate import *
from db_operation.insurance_operate import *
from db_operation.product_operate import insert_product
from db_operation.project_operate import *
from db_operation.order import *
import db_operation.employee_operate as db_emp_opr
from db_operation.test.read import read
from db_operation.database_basic.database_operate import recreate_table


def test_for_insert():

    # s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\user.csv')
    # for item in s:
    #     insert_user(item)
    # s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\project.csv')
    s = read(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db_operation\test\project.csv')
    for item in s:
        insert_product(item)
        insert_project(item)

    # s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\insurance.csv')
    # for item in s:
    #     add_insurance(item)
    #
    # s = read(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\order.csv')
    #
    # for item in s:
    #     add_order(item)
    print('insert project and product successfully')

def test_for_update():
    print('update successfully')

def test_for_delete():
    print('delete successfully')

def test_for_search():
    # with open('out_search.txt','w') as f:
    #     f.write('{}\n'.format(search_order()))
    print('search successfully')

def test_for_user_all_function():
    with open('out_all_insurance.txt','w') as f:
        for item in user_all_insurance('AngelaChristopher'):
            f.write('{}\n'.format(item))
    with open('out_all_order.txt','w') as f:
        for item in get_order('AngelaChristopher'):
            f.write('{}\n'.format(item))
    print('test_for_user_all_function successfully')

def test_insert_employee():
    db_emp_opr.create('e@emp123', '123456')
    print('Insert employee successfully')


if __name__=='__main__':
    # recreate_table()
    test_for_insert()
    test_insert_employee()
    # test_for_search()
    # test_for_update()
    # test_for_delete()
    # test_for_search()
    # test_for_user_all_function()