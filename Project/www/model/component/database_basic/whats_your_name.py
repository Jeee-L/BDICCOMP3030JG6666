from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import yaml


app = Flask(__name__)
# db = yaml.load(open('/var/Project/www/db.yaml'))
db = yaml.load(open('www\db.yaml'))


app.config['SQLALCHEMY_DATABASE_URI'] = db['sqlalchemy_database_uri_local']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(32), nullable=False, unique=True,primary_key=True,  index=True)
    password = db.Column(db.String(32), nullable=False, unique = True)
    phone_num = db.Column(db.Integer, nullable=False, unique = True,  index=True)
    passport_num = db.Column(db.Integer, nullable=False, unique=True,  index=True)
    email = db.Column(db.String(32), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.name



class Passport(db.Model):
    __tablename__ = 'passport'
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    first_name = db.Column(db.String(32), nullable=False, unique=True,  index=True)
    last_name = db.Column(db.String(32), nullable=False, unique=True, index=True)
    birth_day = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(32), nullable=False)
    def __repr__(self):
        return '<User %r %r, passport_id %r>' %(self.first_name,self.last_name,self.id)

class Insurance(db.Model):
    __tablename__ = 'Insurance'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), db.ForeignKey('users.name'))
    product_id = db.Column(db.Integer, nullable=False)
    amount_of_money = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(32), nullable=False)
    flight_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return '<id %r,status id %r>' %(self.id ,self.status)

class Claim(db.Model):
    __tablename__='Claim'
    insurance_id = db.Column(db.Integer, db.ForeignKey('Insurance.id'),nullable=False,unique=True)
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    employee_id = db.Column(db.Integer,nullable = False)
    reason = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<id %r,status id %r>' %(self.id ,self.status)

class Employee(db.Model):
    __tablename__='Employee.model'
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    def __repr__(self):
        return '<id %r,password id %r>' %(self.id ,self.password)

class Administrator(db.Model):
    __tablename__ = 'Administrator.model'
    id = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    def __repr__(self):
        return '<id %r,password id %r>' %(self.id ,self.password)