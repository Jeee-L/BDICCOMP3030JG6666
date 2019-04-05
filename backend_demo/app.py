from flask import Flask,render_template,url_for,request,redirect,g,session,jsonify,make_response
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta
from email_verificatoin import email_verify
from re_verification import *
from flask_cors import core
import model.component.users_operate as usr_opr

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=7)
app.send_file_max_age_default = timedelta(seconds=10)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    user = session.get('username')
    if user:
        return redirect('/1/')
    else:
        return redirect('/0/')

@app.route('/<is_login>/')
def home_page(is_login):
    if is_login == '1':
        return render_template('homepage.html',user=session['username'])
    else:
        return render_template('homepage.html')

@app.route('/login/',methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['comfirm_password']
        if password == confirm_password:
            if verify_password(password):
                if verify_username(username):
                    if usr_opr.search_username(username):
                        if usr_opr.password_is_right(password):
                            return "登陆成功"
                        else:
                            "密码不正确"
                    else:
                        return "用户不存在"
                else:
                    return "用户名不合法"
            else:
                return "密码不合法"
        else:
            return "两次输入密码不相等"


@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        register_info = {}
        register_info['username'] = request.form['username']
        register_info['password'] = request.form['password']
        register_info['confirm_password'] = request.form['confirm_password']
        register_info['passport'] = request.form['passport']
        register_info['phone'] = request.form['phonenumber']
        register_info['email'] = request.form['email']
        verify_result = verify_register_info(register_info)
        if verify_result:
            pass
        else:
            return verify_result


def verify_register_info(register_info):
    if verify_username(register_info['username'])


@app.route('/success/')
def success_page():
    return render_template('successpage.html')

@app.route('/failure/')
def failure_page():
    return render_template('register_failpage.html')

@app.route('/deatil/',methods=['GET','POST'])
def detail_page():
    if request.method == 'POST':
        if request.form['alteredname'] is not None:
            altered_username = request.form['alteredname']
        if request.form['alteredpassword'] is not None:
            altered_password = request.form['alteredpassword']
        if request.form['alteredphone'] != '':
            altered_phone = request.form['alteredphone']
        if request.form['alteredemail'] != '':
            altered_email = request.form['alteredemail']
        # passport

        user_image = request.files['user_icon']
        if not (user_image and allowed_file(user_image.filename)):
            # 返回一个Json文件格式错误
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
        user_input = request.form.get("name")
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/user_images', secure_filename(user_image.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        user_image.save(upload_path)

        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/user_images', 'test.jpg'), img)

        return render_template('detail_withicon.html', user_icon=user_input, val1=time.time())

        # return render_template('successpage.html')
    else:
        return render_template('detail.html')

@app.route('/claimpage/',methods=['GET','POST'])
def claim_page():
    if request.method == 'POST':
        luggage_image = request.files['luggage_icon']
        if not (luggage_image and allowed_file(luggage_image.filename)):
            # 返回一个Json文件格式错误
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
        luggage_input = request.form.get("name")
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/luggage_images',secure_filename(luggage_image.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        luggage_image.save(upload_path)

        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/luggage_images', 'test.jpg'), img)

        description = request.form.get('description')
        print(description)

        return render_template('claimpage_withimage.html', user_icon=luggage_input, val1=time.time())
    else:
        return render_template('claimpage.html')

@app.route('/verify/',methods=['GET','POST'])
def verify_email_page():
    if request.method == 'POST':
        user_email = request.form['email_address']
        verification_code = email_verify(user_email)
        return render_template('successpage.html')
    else:
        return render_template('verify_eamilpage.html')

@app.route('/logout/')
def logout_page():
    session.clear()
    return render_template('loginpage.html')


if __name__ == '__main__':
    app.run()
