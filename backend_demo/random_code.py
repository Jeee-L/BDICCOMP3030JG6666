import string, random
def random_code_generator():
    src_upp = string.ascii_uppercase
    src_let = string.ascii_lowercase
    src_num = string.digits

    upp_c = random.randint(1, 6)
    low_c = random.randint(1, 8 - upp_c - 1)
    num_c = 8 - (upp_c + low_c)
    # 随机生成密码
    password = random.sample(src_upp, upp_c) + random.sample(src_let, low_c) + random.sample(src_num, num_c)
    # 打乱列表元素
    random.shuffle(password)
    # 列表转换为字符串
    new_password = ''.join(password)

    return new_password
