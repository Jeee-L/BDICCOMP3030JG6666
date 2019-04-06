from re_verification import *
import db_operatoin.users_operate as db_usr_opr
import db_operatoin.insurance_operate as db_ins_opr
import db_operatoin.claim_operate as db_cla_opr
import os
import cv2
from werkzeug.utils import secure_filename

def login(username,password,confirm_password):
    if not (password == confirm_password):
        return "两次输入密码不相等"
    elif not verify_password(password):
        return "密码不合法"
    elif not verify_username(username):
        return "用户名不合法"
    elif db_usr_opr.search_username(username):
        return "用户不存在"
    elif db_usr_opr.password_is_right(password):
        return "密码不正确"
    else:
        return "登陆成功"

def register(register_info):
    verify_result = verify_register_info(register_info)
    if verify_result:
        try:
            db_usr_opr.insert_user(register_info)
        except AssertionError as ae:
            return ae
    else:
        return verify_result

def verify_register_info(register_info):
    if not verify_username(register_info['name']):
        return "用户名不合法"
    elif not (register_info['password']==register_info['confirm_password']):
        return "两次输入密码不一样"
    elif not verify_password(register_info['password']):
        return "密码不合法"
    elif not verify_email(register_info['email']):
        return "邮箱不合法"
    elif not verify_phone_number(register_info['phone_num']):
        return "手机号不合法"
    elif not verify_passport(register_info['passport_num']):
        return "护照号不合法"
    else:
        return True

def update_name(old_name,new_name):
    # TODO 如何获得用户的 old_name?
    if not verify_username(new_name):
        return "新用户名不合法"
    else:
        try:
            return db_usr_opr.update_username(old_name,new_name)
        except AssertionError as ae:
            return ae

def update_password(name,new_password,confirme_password):
    if not verify_password(new_password):
        return "新密码不合法"
    elif not (new_password == confirme_password):
        return "两次输入的密码不一样"
    else:
        try:
            return db_usr_opr.update_password(name,new_password)
        except AssertionError as ae:
            return ae

def update_email(name,new_email):
    if not verify_email(new_email):
        return "邮箱格式不合法"
    else:
        try:
            return db_usr_opr.update_email(name,new_email)
        except AssertionError as ae:
            return ae

def update_phone(name,new_phone):
    if not verify_phone_number(new_phone):
        return "手机号格式不合法"
    else:
        try:
            return db_usr_opr.update_phone_num(name,new_phone)
        except AssertionError as ae:
            return ae

def update_passport(name,new_passport):
    if not verify_passport(new_passport):
        return "护照号格式不合法"
    else:
        try:
            return db_usr_opr.update_passport_num(name,new_passport)
        except AssertionError as ae:
            return ae

# 图片允许的后缀名
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'r') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream

def update_user_image(name,user_image):
    if not (user_image and allowed_file(user_image.filename)):
        # 返回一个Json文件格式错误
        # return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
        return "图片类型不合法,仅限于png、PNG、jpg、JPG、bmp"
    basepath = os.path.dirname(__file__)  # 当前文件所在路径

    # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    upload_path = os.path.join(basepath, 'static/user_images',
                               secure_filename(user_image.filename))
    user_image.save(upload_path)

    byte_size = os.path.getsize(upload_path)
    MB_size = float(byte_size / (1024 * 1024))
    if not (MB_size < 2):
        return "图片大小不可超出 2 MB"

    # 使用Opencv转换一下图片格式和名称
    img = cv2.imread(upload_path)
    cv2.imwrite(os.path.join(basepath, 'static/user_images', 'temp_user_avatar.jpg'), img)

    image_stream = img_stream(basepath+'static/user_images/temp_user_avatar')

    try:
        db_usr_opr.update_profile(name,image_stream)
        os.remove(upload_path)
        return "头像上传成功"
    except AssertionError as ae:
        return "头像上传失败"

def convert_insurance_image(insurance_image):
    if not (insurance_image and allowed_file(insurance_image.filename)):
        return "图片类型不合法,仅限于png、PNG、jpg、JPG、bmp"
    basepath = os.path.dirname(__file__)  # 当前文件所在路径

    # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    upload_path = os.path.join(basepath, 'static/insurance_images',
                               secure_filename(insurance_image.filename))
    insurance_image.save(upload_path)

    byte_size = os.path.getsize(upload_path)
    MB_size = float(byte_size / (1024 * 1024))
    if not (MB_size < 2):
        return "图片大小不可超出 2 MB"

    # 使用Opencv转换一下图片格式和名称
    img = cv2.imread(upload_path)
    cv2.imwrite(os.path.join(basepath, 'static/insurance_images', 'temp_insurance_image.jpg'), img)

    image_stream = img_stream(basepath+'static/insurance_images/temp_insurance_image')

    image_info = [image_stream,upload_path]
    return image_info

def buy_insurance(insurance_info):
    try:
        insurance_image_info = convert_insurance_image(insurance_info['image'])
        insurance_info['image'] = insurance_image_info[0]
        upload_path = insurance_image_info[1]
        insurance_id = db_ins_opr.add_insurance(insurance_info)
        os.remove(upload_path)
        # 返回保险号
        return insurance_id
    except AssertionError as ae:
        return "购买失败,reason: "+ae

def user_all_insurance(username):
    # TODO 查找这个用户名下的所有保险
    pass

def apply_claim(claim_info):
    if not (len(claim_info['reason'])<300):
        return "原因长度在300个字符以内"
    try:
        return db_cla_opr.add_claim(claim_info)
    except AssertionError as ae:
        return "失败, reason: "+ae

def user_all_claim(username):
    # TODO 用户所有的理赔申请
    pass