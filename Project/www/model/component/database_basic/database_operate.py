from www.model.component.database_basic.whats_your_name import db

def create_tables():
    '建表'
    db.create_all()
    return 'Create successfully'


def drop_all_tables():
    '删库跑路'
    db.drop_all()
    return 'Drop successfully'

def recreate_table():
    create_tables()
    drop_all_tables()
    print('create successfully')

if __name__ == '__main__':
    recreate_table()