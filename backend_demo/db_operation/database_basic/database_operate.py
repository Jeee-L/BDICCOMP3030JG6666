
from backend_demo.db_operation.database_basic.whats_your_name import db


def create_tables():
    '''

    :return:'Create successfully'
    '''
    db.create_all()
    return 'Create successfully'


def drop_all_tables():
    '''

    :return:'Drop successfully'
    '''
    db.drop_all()
    return 'Drop successfully'

def recreate_table():
    '''

    :return:
    '''
    drop_all_tables()
    create_tables()
    print('create successfully')

if __name__ == '__main__':
    recreate_table()