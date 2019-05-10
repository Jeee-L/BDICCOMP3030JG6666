import smtplib
from email.mime.text import MIMEText
from email.header import Header
from random_code import random_code_generator

def email_verify(reciever_email):

    # 第三方 SMTP 服务：163邮箱
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "hibernia_sino@163.com"  # 用户名
    mail_pass = "ShouQuan2019"  # 授权码

    sender = 'hibernia_sino@163.com'
    receivers = reciever_email  # 接收邮件

    verification_code = random_code_generator()

    content = "这是您的验证码："+ str(verification_code)+"，请妥善保管\n"+ "This is your verifiecation code, please keep it well: "+ str(verification_code)

    # content = """
    #     <h1>这是标题</h1>
    #     <p>
    #     这是验证码:
    #     """+verification_code+"""
    #
    #     </p>
    #
    # """

    message = MIMEText(content, 'plain', 'utf-8')
    # message = MIMEText(content, 'html', 'utf-8')
    message['From'] = mail_user
    message['To'] = receivers

    subject = '来自HS的验证码邮件/Verification code mail from HS '
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        return verification_code
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)
        return '0'

