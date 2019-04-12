import datetime

from flask_sqlalchemy import SQLAlchemy,event
from flask import Flask
from werkzeug.security import generate_password_hash,check_password_hash

import yaml
from backend_demo.ext import db
# app =  Flask(__name__)
# dbs = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)
# app.config['SQLALCHEMY_DATABASE_URI'] = dbs['sqlalchemy_database_uri_local']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = yaml.load(open('/var/Project/www/db.yaml'))
# db = yaml.load(open(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\Project\www\db.yaml'))

# db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = 'users'
    first_name = db.Column(db.String(32), nullable=True, index=True)
    last_name = db.Column(db.String(32), nullable=True, index=True)
    username = db.Column(db.String(32), nullable=False, unique=True,primary_key=True,  index=True)
    password_hash = db.Column(db.String(300), nullable=False)
    phone_num = db.Column(db.String(13), nullable=False, unique = False,  index=True)
    passport_num = db.Column(db.String(13), nullable=True, unique=True,  index=True)
    email = db.Column(db.String(32), nullable=True, unique=True)
    profile = db.Column(db.LargeBinary(length=204800))
    birthday = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(32), nullable=True)
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
        first_name = {}
        last_name = {}
        username = {}
        phone_num = {}
        passport_num = {}
        email = {}
        birth_day = {}
        address = {}
        '''.format(self.first_name,self.last_name,self.username,self.phone_num,self.passport_num,self.email, self.birthday, self.address )




class Insurance(db.Model):
    __tablename__ = 'Insurance'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), db.ForeignKey('users.username'))
    pro_id = db.Column(db.Integer, nullable=False)
    amount_of_money = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(32), nullable=False)
    flight_number = db.Column(db.Integer, nullable=False)
    luggage_image_outside = db.Column(db.LargeBinary(length=204800))
    luggage_image_inside = db.Column(db.LargeBinary(length=204800))
    luggage_height = db.Column(db.Integer, nullable=False)
    luggage_width = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())
    claim_id = db.relationship('Claim', backref='insurance',
                                lazy='dynamic')
    remark = db.Column(db.String(32))
    def __repr__(self):
        return '''
        id = {}
        username = {}
        pro_id = {}
        amount_of_money = {}
        status = {}
        flight_number = {}
        luggage_height = {}
        luggage_width = {}
        date = {}
        claim_id = {}
        remark = {}
        '''.format(self.id, self.username,self.pro_id,self.amount_of_money, self.status, self.flight_number,self.luggage_height,self.luggage_width,self.date, self.claim_id,self.remark)



class Claim(db.Model):
    __tablename__='Claim'
    insurance_id = db.Column(db.Integer, db.ForeignKey('Insurance.id'),nullable=False,unique=True)
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True,autoincrement=True)
    employee_id = db.Column(db.Integer,nullable = False)
    reason = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    lost_time = db.Column(db.DateTime, nullable=False)
    lost_place = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    remark = db.Column(db.String(300), nullable=False)
    def __repr__(self):
        return '''
        insurance_id = {}
        id = {}
        employee_id = {}
        reason = {}
        status = {}
        lost_time = {}
        lost_place = {}
        remark = {}
        '''.format(self.insurance_id, self.id, self.employee_id,self.reason, self.status, self.lost_time,self.lost_place,self.remark)






class Employee(db.Model):
    __tablename__='Employee'
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    password_hash = db.Column(db.String(32), nullable=False, unique=True)

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
    __tablename__ = 'Administrator'
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    password_hash = db.Column(db.String(32), nullable=False, unique=True)

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
        '''.format(id)



class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, nullable=False, primary_key=True)
    product_information = db.Column(db.String(300))
    def __repr__(self):
        return '''
        product_id = {}
        product_information = {}
        '''.format(self.product_id, self.product_information)



class Project(db.Model):
    __tablename__ = 'Project'
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), primary_key = True)
    project_id = db.Column(db.Integer, nullable = False, primary_key = True)
    coverage = db.Column(db.Integer, nullable=False)
    The_amount_of_each_shipment_insured = db.Column(db.Integer, nullable = False)
    premium = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '''
        project_id = {}
        coverage = {}
        The_amount_of_each_shipment_insured = {}
        premium = {}
        '''.format(self.project_id, self.coverage, self.The_amount_of_each_shipment_insured, self. premium)

class log(db.Model):
    __tablename__ = 'log'
    date = db.Column(db.DateTime, nullable=False, primary_key = True)
    employee_id = db.Column(db.Integer, nullable=False, primary_key = True)

# @event.listens_for(Insurance.amount_of_money,'set')
# def set_to_log(target, value,oldvalue, initiator):
#     logs = log()
#     db.session.add(logs)
#     db.session.commit()


