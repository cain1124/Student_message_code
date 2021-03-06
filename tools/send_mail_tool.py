from users.models import EmailVerifyCode
# from random import choice
from random import randrange
from django.core.mail import send_mail
from djangoProject.settings import EMAIL_FROM


def get_random_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' #码源
    code = ''
    for i in range(code_length):
        #随机选择一个字符
        # code += choice(code_source)  可以采用这种方法随机选取字符
        str = code_source[randrange(0, len(code_source)-1)]
        code += str
    return code


def send_email_code(email, send_type):
    #第一步，创建邮箱验证码对象，保存到数据库，用来以后做对比
    code = get_random_code(6)
    a = EmailVerifyCode()   #实例化
    a.email = email
    a.send_type = send_type
    a.code = code
    a.save()
    #第二步，正式发送邮件
    send_title = ''
    send_body = ''
    #激活账号邮箱邮件
    if send_type == 1:
        send_title = '欢迎注册学生信息系统：'
        send_body = '请点击以下链接进行激活您的账号：\n http://127.0.0.1:8000/users/user_active/'+code
        send_mail(send_title, send_body, EMAIL_FROM, [email])  #发送邮件
    #重置密码邮箱邮件
    if send_type == 2:
        send_title = '学生信息系统重置密码操作：'
        send_body = '请点击以下链接进行重置您的密码：\n http://127.0.0.1:8000/users/user_reset/' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])  # 发送邮件
    # 修改邮箱账号邮箱邮件
    if send_type == 3:
        send_title = '学生信息系统修改邮箱操作：'
        send_body = '您的验证码是：'+code
        send_mail(send_title, send_body, EMAIL_FROM, [email])  # 发送邮件