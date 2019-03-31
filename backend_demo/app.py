from flask import Flask,render_template,url_for,request,redirect,g,session,jsonify,make_response
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta
from email_verificatoin import email_verify


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
    # user = request.cookies.get('username')
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

        session['username'] = username
        session.permanent = True

        # search in the database to check whether this user is valid
        return redirect('/1/')
    else:
        return render_template('loginpage.html')

@app.route('/register/',methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phonenumber']
        email = request.form['email']
        check_password = request.form['check_password']
        print("username: "+username+" password: "+password)
        if check_password == password and password != '':
            # search in database
            return redirect(url_for('success_page'))
        else:
            return redirect(url_for('failure_page'))
    else:
        return render_template('registerpage.html')

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
