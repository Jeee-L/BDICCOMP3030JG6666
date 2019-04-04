from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import generate_password_hash,check_password_hash
from flask_security import RoleMixin, UserMixin
import yaml


app = Flask(__name__)
# db = yaml.load(open('/var/Project/www/db.yaml'))
db = yaml.load(open('C:\\Users\\TED\\Documents\\GitHub\\MySimplePythonCode\\BDICCOMP3030JG6666\\Project\\www\\db.yaml'))


app.config['SQLALCHEMY_DATABASE_URI'] = db['sqlalchemy_database_uri_local']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    name = db.Column(db.String(32), nullable=False, unique=True,primary_key=True,  index=True)
    password_hash = db.Column(db.String(300), nullable=False, unique = True)
    phone_num = db.Column(db.Integer, nullable=False, unique = True,  index=True)
    passport_num = db.Column(db.Integer, nullable=False, unique=True,  index=True)
    email = db.Column(db.String(32), nullable=False, unique=True)

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    # 转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


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