# 图片允许的后缀名
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#
#
# def img_stream(img_local_path):
#     """
#     工具函数:
#     获取本地图片流
#     :param img_local_path:文件单张图片的本地绝对路径
#     :return: 图片流
#     """
#     import base64
#     img_stream = ''
#     with open(img_local_path, 'r') as img_f:
#         img_stream = img_f.read()
#         img_stream = base64.b64encode(img_stream)
#     return img_stream

# if not (user_image and allowed_file(user_image.filename)):
#     return jsonify({"state": '0', "error_msg": "Illegal image type，limited: png、PNG、jpg、JPG、bmp"})
# basepath = os.path.dirname(__file__)  # 当前文件所在路径
#
# # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
# upload_path = os.path.join(basepath, 'static/user_images',
#                            secure_filename(user_image.filename))
# user_image.save(upload_path)
#
# byte_size = os.path.getsize(upload_path)
# MB_size = float(byte_size / (1024 * 1024))
# if not (MB_size < 2):
#     return jsonify({"state": '0', "error_msg": "image size should not bigger than 2 MB"})
#
# # 使用Opencv转换一下图片格式和名称
# img = cv2.imread(upload_path)
# cv2.imwrite(os.path.join(basepath, 'static/user_images', 'temp_user_avatar.jpg'), img)
#
# image_stream = img_stream(basepath + 'static/user_images/temp_user_avatar')

# if len(user_image) > 204800:
#     return jsonify({"state": '0', "error_msg": "Image size should not bigger than 2 MB"})