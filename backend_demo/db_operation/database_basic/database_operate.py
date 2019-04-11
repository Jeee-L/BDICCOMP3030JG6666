from db_operation.database_basic.whats_your_name import db
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from ext import db
# app = Flask(__name__)
# dbs = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)
# app.config['SQLALCHEMY_DATABASE_URI'] = dbs['sqlalchemy_database_uri_local']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
# db  = SQLAlchemy(app)
def create_tables():
    '建表'
    db.create_all()
    return 'Create successfully'


def drop_all_tables():
    '删库跑路'
    db.drop_all()
    return 'Drop successfully'

def recreate_table():
    drop_all_tables()
    create_tables()
    print('create successfully')

if __name__ == '__main__':
    recreate_table()