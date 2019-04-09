import datetime

from flask_sqlalchemy import SQLAlchemy,event
from flask import Flask
from werkzeug.security import generate_password_hash,check_password_hash

import yaml


app = Flask(__name__)
# db = yaml.load(open('/var/Project/www/db.yaml'))
# db = yaml.load(open(r'C:\Users\TED\Documents\GitHub\MySimplePythonCode\BDICCOMP3030JG6666\Project\www\db.yaml'),Loader=yaml.FullLoader)
# db = yaml.load(open(r'/Users/pro13/Desktop/Study/3Junior/SecondSemester/SEP2/GitRepository/BDICCOMP3030JG6666/Project/www/db.yaml'),Loader=yaml.FullLoader)
db = yaml.load(open(r'C:\SoftwareProject2\BDICCOMP3030JG6666\backend_demo\db.yaml'),Loader=yaml.FullLoader)

app.config['SQLALCHEMY_DATABASE_URI'] = db['sqlalchemy_database_uri_local']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = 'users'
    first_name = db.Column(db.String(32), nullable=True, index=True)
    last_name = db.Column(db.String(32), nullable=True, index=True)
    username = db.Column(db.String(32), nullable=False, unique=True,primary_key=True,  index=True)
    password_hash = db.Column(db.String(300), nullable=False)
    phone_num = db.Column(db.Integer, nullable=False, unique = False,  index=True)
    passport_num = db.Column(db.Integer, nullable=True, unique=True,  index=True)
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

    @classmethod
    def search_username(cls,username):
        '''
        查找用户
        :param username: 用户名
        :return: 用户对象 or None
        '''
        return cls.query.filter_by(username=username).first()

    @classmethod
    def password_is_right(cls,username, password):
        '''
        查找密码是否正确
        :param username: 用户名
        :param password: 明文密码
        :return: True or False
        '''
        user = cls.search_username(username)
        return user.check_password_hash(password)

    @classmethod
    def insert_user(cls,dict):
        '''
        插入用户
        :param dict: 用户信息字典
        :return: 是否创建成功
        '''
        user = cls.search_username(dict['username'])
        db.session.add(Users(username=dict['username'], password=dict['password'], phone_num=dict['phone_num'],
                             email=dict['email']))
        db.session.commit()
        return 'Create successfully'

    @classmethod
    def get_insurance(cls,username):
        '''
        获得用户的所有保险
        :param username: 用户名
        :return: list
        '''
        user = cls.search_username(username)
        return user.insurance_id.all()

    @classmethod
    def get_claim(cls,username):
        '''
        获得用户的所有申报
        :param username:用户名
        :return: list
        '''
        user = cls.search_username(username)
        return user.claim_id.all()

    @classmethod
    def update_profile(cls,username, new_profile):
        '''
        上传用户照片
        :param username: 用户名
        :param new_profile: 新照片
        :return: 是否创建成功
        '''
        user = cls.search_username(username)
        user.profile = new_profile
        db.session.commit()
        return "Update successfully"

    @classmethod
    def update_username(cls,username, new_name):
        '''
        更新用户名
        :param username:用户名
        :param new_name: 新名称
        :return: 是否创建成功
        '''
        user = cls.search_username(username)
        user.username = new_name
        db.session.commit()
        return "Update successfully"

    @classmethod
    def update_password(cls,username, new_password):
        '''
        更新密码
        :param username: 用户名
        :param new_password: 新密码
        :return: 是否更新成功
        '''
        user = cls.search_username(username)
        user.password = new_password
        return "Update successfully"

    @classmethod
    def update_phone_num(cls,username, new_phone_num):
        '''
        更新手机号
        :param username:用户名
        :param new_phone_num: 手机号
        :return: 是否更新成功
        '''
        user = cls.search_username(username)
        user.phone_num = new_phone_num
        return "Update successfully"

    @classmethod
    def update_passport_num(cls,username, new_passport_num):
        '''
        更新护照id
        :param username: 用户名
        :param new_passport_num: 护照id
        :return: 是否更新成功
        '''
        user = cls.search_username(username)
        user.password = new_passport_num
        return "Update successfully"

    @classmethod
    def update_email(cls,username, new_email):
        user = cls.search_username(username)
        user.password = new_email
        return 'Update email successfully'

    @classmethod
    def delete_user(cls,username):
        user = cls.search_username(username)
        db.session.delete(user)
        db.session.commit()
        return 'Delete successfully'


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

    @classmethod
    def __search_insurance(cls,id):
        return Insurance.query.filter_by(id=id).first()

    @classmethod
    def add_insurance(cls,dict):
        'id,name[0],product_id[1],amount_of_money[2],status,flight_number[3]'
        'status are the one of set (Creating, using, out_date)'
        assert (Users.search_username(dict['username']) is not None), "No such User"
        f = Insurance(username=dict['username'], product_id=dict['product_id'], amount_of_money=dict['amount_of_money'],
                      flight_number=dict['flight_number'], status=dict['status'], luggage_image_outside=dict['luggage_image_outside'], luggage_image_inside=dict['luggage_image_inside'],luggage_height=dict['luggage_height'],
                      luggage_width=dict['luggage_width'])
        db.session.add(f)
        db.session.commit()
        return f.id

    @classmethod
    def change_staue(cls, id, state):
        ins = Insurance.__search_insurance(id)
        assert ins is not None, 'No such Insurance'
        ins.status = state
        return 'Change successfully'

    @classmethod
    def all(cls):
        return Insurance.query.all()

    @classmethod
    def search_claim(cls,ins):
        return ins.claim_id.first()

    @classmethod
    def user_all_insurance(cls, username):
        return Insurance.query.filter_by(username=username).all()


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

    @classmethod
    def add_claim(cls, dict):
        '''
        :param dict:
        :return:
        '''
        assert (Insurance.__search_insurance(id) is not None), 'No such insurance id'
        db.session.add(Claim(insurance_id=dict['insurance_id'], employee_id=dict['employee_id'], reason=dict['reason'],
                             status=dict['status']))
        db.session.commit()
        return 'Create Claim successfully'

    @classmethod
    def search_claim_use_insurance_id(cls, id):
        return Claim.query.filter_by(insurance_id=id).all()

    @classmethod
    def __search_claim(cls, id):
        return Claim.query.filter_by(id=id).first()

    @classmethod
    def cancel_claim(cls, id):
        claim =Claim.__search_claim(id)
        assert (claim is not None), 'No such Claim'
        claim.status = 'cancel'
        return 'cancel Successfully'

    @classmethod
    def change_staue(cls, id, state):
        claim = Claim.__search_claim(id)
        assert claim is not None, 'No such Claim'
        claim.status = state
        return 'Change successfully'

    @classmethod
    def all(cls):
        return Claim.query.all()


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

    @classmethod
    def search_id(cls, id):
        return Employee.query.filter_by(id=id).first()

    @classmethod
    def login(cls, id, password):
        emp = Employee.search_id(id)
        assert (emp is not None), 'No such id'
        assert (emp.check_password_hash(password)), 'Wrong password'
        return "Login successfully"

    @classmethod
    def create(cls, id, password):
        emp = Employee.search_id(id)
        assert (emp is not None), 'Already exist'
        db.session.add(Employee(id=id, password=password))
        db.session.commit()
        return 'Create employee Successfully'

    @classmethod
    def update_password(cls, id, new_password):
        emp = Employee.query.filter_by(id=id).first()
        assert (emp is not None), "No such employee"
        assert (not emp.check_password_hash(new_password)), "New password is same as old Password"
        emp.password = new_password
        return 'Update password successfully'

    @classmethod
    def delete(cls, id):
        emp = Employee.query.filter_by(id=id).first()
        assert (emp is not None), "No such employee"
        db.session.delete(emp)
        db.session.commit()
        return 'successful'



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

    @classmethod
    def search_id(id):
        return Administrator.query.filter_by(id=id).first()

    @classmethod
    def login(id, password):
        admin = Administrator.search_id(id)
        assert (Administrator.search_id(id) is not None), 'No such id'
        assert (admin.check_password_hash(password)), 'Password wrong'
        return 'Login successfully'

    @classmethod
    def create(id, password):
        assert (Administrator.search_id(id) is None), 'Administrator already exist'
        db.session.add(Administrator(id=id, password=password))
        db.session.commit()
        return 'Create successfully'

    @classmethod
    def update_password(id, new_password):
        '''

        :param new_password:
        :return:
        '''
        admin = Administrator.search_id(id)
        assert (admin is not None), 'No such administrator'
        assert (not admin.check_password_hash(new_password)), 'Same password'
        admin.password = new_password
        return 'Update successfully'

    @classmethod
    def delete(cls, id):
        '''

        :param id: administrator id
        :return: string
        '''
        admin = Administrator.search_id(id)
        db.session.delete(admin)
        db.session.commit()
        return 'Delete successfully'

    @classmethod
    def delete_employee(cls, id):
        '''

        :param id:
        :return:
        '''
        return Employee.delete(id)

    @classmethod
    def update_employee_password(cls, id, password):
        '''

        :param id:
        :param password:
        :return:
        '''
        return Employee.update_password(id, password)

    @classmethod
    def create_employee(cls, id, password):
        '''

        :param id:
        :param password:
        :return:
        '''
        return Employee.create(id, password)

    @classmethod
    def search_employee(cls, id):
        '''

        :param id:
        :return:
        '''
        return Employee.Administrator.search_id(id)

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



