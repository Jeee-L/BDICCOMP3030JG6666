import datetime
from flask_sqlalchemy import SQLAlchemy,event
from flask import Flask
from werkzeug.security import generate_password_hash,check_password_hash
import yaml


# app =  Flask(__name__)
# # dbs = yaml.load(open('/var/Project/www/db.yaml'), Loader=yaml.FullLoader)
# dbs = yaml.load(open(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\backend_demo\db_operation\test\db.yaml'), Loader=yaml.FullLoader)
# # dbs = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)
# app.config['SQLALCHEMY_DATABASE_URI'] = dbs['sqlalchemy_database_uri_local']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
'''
创建库的时候，注释取消
'''


from backend_demo.ext import db
'''
启动服务前，注释取消
'''


'''
两组注释有且只能有一个
'''

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique= True, index=True, autoincrement=True, primary_key=True)
    first_name = db.Column(db.Unicode(32), nullable=True)
    last_name = db.Column(db.Unicode(32), nullable=True)
    username = db.Column(db.Unicode(32), nullable=False, unique=True)
    password_hash = db.Column(db.Unicode(300), nullable=True)
    phone_num = db.Column(db.Unicode(13), nullable=True, unique = False)
    passport_num = db.Column(db.Unicode(13), nullable=True, unique=True)
    email = db.Column(db.Unicode(32), nullable=True, unique=True)
    profile = db.Column(db.LargeBinary(length=204800))
    birthday = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.Unicode(32), nullable=True)
    insurance_id = db.relationship('Insurance', backref='users',
                                   lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '''
        ***************
        first_name = {}
        last_name = {}
        username = {}
        phone_num = {}
        passport_num = {}
        email = {}
        birth_day = {}
        address = {}
        ***************
        '''.format(self.first_name,self.last_name,self.username,self.phone_num,self.passport_num,self.email, self.birthday, self.address )

class Order(db.Model):
    __tablename__ = 'order'
    # insurance_order
    # insurance_id Foreign
    # state
    # employee gai这个状
    order_id = db.Column(db.Integer, primary_key = True, auto_increment = True, unique = True)
    state = db.Column(db.Integer)
    insurance_id = db.relationship('Insurance', backref='order',
                                   lazy = 'dynamic')
    flight_number = db.Column(db.Integer, nullable=True)
    luggage_image_outside = db.Column(db.LargeBinary(length=204800), nullable=True)
    luggage_image_inside = db.Column(db.LargeBinary(length=204800), nullable=True)
    luggage_height = db.Column(db.Integer, nullable=True)
    luggage_width = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    claim_id = db.relationship('Claim', backref='order',
                               lazy='dynamic')
    remark = db.Column(db.Unicode(32))



class Insurance(db.Model):
    __tablename__ = 'insurance'
    id = db.Column(db.Integer, nullable=True, primary_key=True, autoincrement=True)
    username = db.Column(db.ForeignKey('users.username', ondelete='CASCADE',onupdate='CASCADE'))
    project_id = db.Column(db.ForeignKey('project.project_id', ondelete='CASCADE', onupdate='CASCADE'), unique=False)
    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE', onupdate='CASCADE'), unique=False)
    amount_of_money = db.Column(db.Integer, nullable=True)
    state = db.Column(db.Unicode(32), nullable=True)
    remark = db.Column(db.Unicode(32))
    compensated_amount = db.Column(db.Integer, nullable = True)
    def __repr__(self):
        return '''
        ***************
        id = {}
        username = {}
        project_id = {}
        product_id = {}
        amount_of_money = {}
        state = {}
        remark = {}
        compensated_amount = {}
        ***************
        '''.format(self.id, self.username,self.project_id,self. product_id,self.amount_of_money, self.state,self.remark,self.compensated_amount)



class Claim(db.Model):
    __tablename__='claim'
    insurance_id = db.Column(db.ForeignKey('insurance.id', ondelete='CASCADE',onupdate='CASCADE'),nullable=True,unique=True)
    id = db.Column(db.Integer, nullable=True, primary_key=True, index=True,autoincrement=True)
    employee_id = db.Column(db.Integer,nullable = False)
    reason = db.Column(db.Unicode(300), nullable=True)
    state = db.Column(db.Integer, nullable=True)
    lost_time = db.Column(db.DateTime, nullable=True)
    lost_place = db.Column(db.Unicode(100), nullable=True)
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    remark = db.Column(db.Unicode(300), nullable=True)
    def __repr__(self):
        return '''
        ***************
        insurance_id = {}
        id = {}
        employee_id = {}
        reason = {}
        state = {}
        lost_time = {}
        lost_place = {}
        time = {}
        remark = {}
        ***************
        '''.format(self.insurance_id, self.id, self.employee_id, self.reason, self.state, self.lost_time,self.lost_place,self.time, self.remark)






class Employee(db.Model):
    __tablename__='Employee'
    id = db.Column(db.Integer, nullable=True, primary_key=True, index=True)
    password_hash = db.Column(db.Unicode(32), nullable=True, unique=True)

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '''
        id = {}
        '''.format(self.id)





class Administrator(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer, nullable=True, primary_key=True, index=True)
    password_hash = db.Column(db.Unicode(32), nullable=True, unique=True)

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '''
        ***************
        id = {}
        password = {}
        ***************
        '''.format(self.id, self.password_hash)



class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    product_information = db.Column(db.Unicode(300))
    def __repr__(self):
        return '''
        ***************
        product_id = {}
        product_information = {}
        ***************
        '''.format(self.product_id, self.product_information)



class Project(db.Model):
    __tablename__ = 'project'
    product_id = db.Column(db.ForeignKey('product.product_id', ondelete='CASCADE',onupdate='CASCADE'),primary_key=True,unique=True )
    project_id = db.Column(db.Integer,  primary_key = True, unique=True)
    coverage = db.Column(db.Integer, nullable=True)
    amount_of_each_shipment_insured = db.Column(db.Integer, nullable = False)
    premium = db.Column(db.Integer, nullable=True)
    def __repr__(self):
        return '''
        ***************
        product_id = {}
        project_id = {}
        coverage = {}
        The_amount_of_each_shipment_insured = {}
        premium = {}
        ***************
        '''.format(self.product_id, self.project_id, self.coverage, self.amount_of_each_shipment_insured, self. premium)

class log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=True)
    previous_money = db.Column(db.Integer, nullable=False)
    post_money = db.Column(db.Integer, nullable=False)


@event.listens_for(Insurance.amount_of_money,'set')
def set_to_log(target, value,oldvalue, initiator):
    '''

    :param target: insurance对象
    :param value: insurance.amout_of_money的值
    :param oldvalue: insurance.amount_of_money原来的值 symbol('NO_VALUE')
    :param initiator: 不知道
    :return: None
    '''
    logs = log(date=datetime.datetime.now(), previous_money=123, post_money=223)
    db.session.add(logs)
    db.session.commit()


