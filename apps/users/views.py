from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import UserLoginForm, UserRegisterForm, UserForgetForm, UserResetForm, UserChangeImageForm,\
   UserChangeEmailForm, UserResetEmailForm, UserChangePwdForm, UserChangeInfoForm, UserExitCourseForm
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from .models import UserProfile, EmailVerifyCode
from course.models import CourseInfo
from department.models import DepartmentInfo, MajorInfo, ClassInfo
from django.core.mail import send_mail
from tools.send_mail_tool import send_email_code
from django.http import JsonResponse
from datetime import datetime
from behavior.models import StudentMessage, ScourseInfo
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage#导入分页包
from django.contrib.auth.decorators import login_required
from tools.decorators import login_decorator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        #这里实例化forms类，目的不是为了验证，而是为了使用验证码
        user_register_form = UserRegisterForm()
        return render(request, 'register.html', {
            'user_register_form': user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            xh = user_register_form.cleaned_data['xh']
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=xh) | Q(xh=xh))
            user_email = UserProfile.objects.filter(email=email)
            if user_list:
                return render(request, 'register.html', {
                    'msg': '该学号已存在'
                })
            elif user_email:
                return render(request, 'register.html', {
                    'msg': '该邮箱已存在'
                })
            else:
                a = UserProfile()
                a.username = xh
                a.xh = xh
                a.email = email
                a.set_password(password)
                a.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            xh = user_login_form.cleaned_data['xh']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username=xh, password=password)
            if user:
                login(request, user)
                #登陆成功，添加一条消息
                a = StudentMessage()
                a.message_student = request.user.id
                a.message_content = '欢迎登陆！'
                a.save()
                course = ScourseInfo.objects.filter(
                    Q(student=request.user, type='已选', course_cj__lt=60) | Q(student=request.user, type='退选',
                                                                             course_cj__lt=60))
                if course:
                    course_list = [course_ver.course.name for course_ver in course]
                    for courses in course_list:
                        msg_ver_list = StudentMessage.objects.filter(message_student=request.user.id,
                                                                     message_content='您选择的' + courses + '课程处于危险状态，请及时查看！')
                        if not msg_ver_list:
                            a = StudentMessage()
                            a.message_student = request.user.id
                            a.message_content = '您选择的'+courses+'课程处于危险状态，请及时查看！'
                            a.save()
                return redirect(reverse('users:user_info'))
            else:
                return render(request, 'login.html', {
                    'msg': '学号或密码错误'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


def user_forget(request):
    if request.method == 'GET':
        return render(request, 'findpwd.html')
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                email_ver_list = EmailVerifyCode.objects.filter(email=email, send_type=2)
                if email_ver_list:
                    email_ver = email_ver_list.order_by('-add_time')[0]
                    if (datetime.now()-email_ver.add_time).seconds > 60:
                        send_email_code(email, 2)
                        email_ver.delete()
                        return HttpResponse('请尽快去您的邮箱重置密码')
                    else:
                        return render(request, 'findpwd.html', {
                            'msg': '请不要重复获取，1分钟后再试'
                        })
                else:
                    send_email_code(email, 2)
                    return HttpResponse('请尽快去您的邮箱重置密码')
            else:
                return render(request, 'findpwd.html', {
                    'msg': '该邮箱不存在'
                })
        else:
            return render(request, 'findpwd.html', {
                'user_forget_form': user_forget_form
            })


#重置密码
def user_reset(request, code):
    if code:
        if request.method == 'GET':
            user_reset_form = UserResetForm()
            return render(request, 'password_reset.html', {
                'user_reset_form': user_reset_form,
                'code': code
            })
        else:
            user_reset_form = UserResetForm(request.POST)
            if user_reset_form.is_valid():
                password = user_reset_form.cleaned_data['password']
                password1 = user_reset_form.cleaned_data['password1']
                if password == password1:
                    email_ver_list = EmailVerifyCode.objects.filter(code=code)
                    if email_ver_list:
                        email_ver = email_ver_list[0]
                        email = email_ver.email
                        user_list = UserProfile.objects.filter(email=email)
                        if user_list:
                            user = user_list[0]
                            user.set_password(password)
                            user.save()
                            return redirect(reverse('users:user_login'))
                        else:
                            pass
                    else:
                        pass
                else:
                    return render(request, 'password_reset.html', {
                        'msg': '两次密码不一致',
                        'code': code
                    })
            else:
                return render(request, 'password_reset.html', {
                    'user_reset_form':user_reset_form,
                    'code': code
                })


@login_decorator
def user_info(request):
    user = request.user
    departments = DepartmentInfo.objects.all()
    return render(request, 'usercenter-info.html', {
        'departments': departments,
        'user': user
    })


# def getMajor(request):
#     major_id = request.GET.get('major_id')
#     majors = MajorInfo.objects.filter(department_id=int(major_id))
#     res = []
#     for i in majors:
#         res.append([i.id, i.name])
#     return JsonResponse({'majors': res})


@login_decorator
def user_changeimage(request):
    user_changeimage_form = UserChangeImageForm(request.POST, request.FILES, instance=request.user)
    if user_changeimage_form.is_valid():
        user_changeimage_form.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'ok'})


@login_decorator
def user_changeemail(request):
    '''
    当用户修改邮箱，点击获取验证码时，会通过这个函数处理，发送邮箱验证码
    :param request: http请求
    :return: 返回json数据，在模板页面中去处理
    '''
    user_changeemail_form = UserChangeEmailForm(request.POST)
    if user_changeemail_form.is_valid():
        email = user_changeemail_form.cleaned_data['email']
        user_list = UserProfile.objects.filter(email=email)
        if user_list:
            return JsonResponse({'status': 'fail', 'msg': '邮箱已被绑定'})
        else:
            email_ver_list = EmailVerifyCode.objects.filter(email=email, send_type=3)
            if email_ver_list:
                email_ver = email_ver_list.order_by('-add_time')[0]
                if (datetime.now() - email_ver.add_time).seconds > 60:
                    send_email_code(email, 3)
                    return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱中获取验证码'})
                else:
                    return JsonResponse({'status': 'fail', 'msg': '请不要重复发送验证码，1分钟后重试'})
            else:
                send_email_code(email, 3)
                return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱中获取验证码'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '请输入合法邮箱'})


@login_decorator
def user_resetemail(request):
    user_resetemail_form = UserResetEmailForm(request.POST)
    if user_resetemail_form.is_valid():
        email = user_resetemail_form.cleaned_data['email']
        code = user_resetemail_form.cleaned_data['code']
        email_ver_list = EmailVerifyCode.objects.filter(email=email, code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            if (datetime.now()-email_ver.add_time).seconds < 60:
                request.user.email = email
                request.user.save()
                return JsonResponse({'status': 'ok', 'msg': '邮箱修改成功'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '验证码失效，请重新发送验证码'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '邮箱或验证码有误'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '请输入规范邮箱或验证码'})


@login_decorator
def user_changepwd(request):
    user_changepwd_form = UserChangePwdForm(request.POST)
    if user_changepwd_form.is_valid():
        password = user_changepwd_form.cleaned_data['password']
        password1 = user_changepwd_form.cleaned_data['password1']
        if password == password1:
            request.user.set_password(password)
            request.user.save()
            return JsonResponse({'status': 'ok', 'msg': '密码修改成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '两次密码输入不一致'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '密码格式不合法'})


@login_decorator
def user_time(request):
    return render(request, 'time.html')


@login_decorator
def user_msg(request):
    msg_list = StudentMessage.objects.filter(message_student=request.user.id).order_by('-add_time')

    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(msg_list, 5)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'message.html', {
        'msg_list': msg_list,
        'pages': pages
    })


@login_decorator
def user_deletemsg(request):
    delete_id = request.GET.get('delete_id', '')
    if delete_id:
        msg = StudentMessage.objects.filter(id=int(delete_id))[0]
        msg.message_status = True
        msg.save()
        return JsonResponse({'status': 'ok', 'msg': '已读'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '读取失败'})


@login_decorator
def user_course(request):
    course_list = ScourseInfo.objects.filter(Q(student=request.user, type='已选') | Q(student=request.user, type='退选')).order_by('-add_time')

    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(course_list, 8)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'course.html', {
        'course_list': course_list,
        'pages': pages
    })


@login_decorator
def user_grade(request):
    course_list = ScourseInfo.objects.filter(
        Q(student=request.user, type='已选') | Q(student=request.user, type='退选')).order_by('-add_time')

    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(course_list, 8)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'grade.html', {
        'course_list': course_list,
        'pages': pages
    })


@login_decorator
def user_changeinfo(request):
    user_changeinfo_form = UserChangeInfoForm(request.POST, instance=request.user)
    if user_changeinfo_form.is_valid():
        phone = user_changeinfo_form.cleaned_data['phone']
        address = user_changeinfo_form.cleaned_data['address']
        request.user.address = address
        if len(phone) == 11:
            request.user.phone = phone
            request.user.save()
            return JsonResponse({'status': 'ok', 'msg': '修改成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '请输入规范手机号'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '请输入合法信息'})


@login_decorator
def user_choosecourse(request):
    scource_list = ScourseInfo.objects.filter(Q(student=request.user, type='已选') | Q(student=request.user, type='退选'))
    scources = [scource.course.name for scource in scource_list]
    apply_ver_list = ScourseInfo.objects.filter(student=request.user, type='申请')
    apply_list = [apply.course for apply in apply_ver_list]
    course_list = CourseInfo.objects.filter(department=request.user.student_department).exclude(name__in=scources).order_by('category')

    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(course_list, 8)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'choose-course.html', {
        'course_list': course_list,
        'apply_list': apply_list,
        'pages': pages
    })


@login_decorator
def user_apply(request):
    course_id = request.GET.get('course_id', '')
    if course_id:
        course = CourseInfo.objects.filter(id=int(course_id))[0]
        apply_ver_list = ScourseInfo.objects.filter(student=request.user, type='申请')
        apply_list = [apply.course for apply in apply_ver_list]
        if course not in apply_list:
            a = ScourseInfo()
            a.student = request.user
            a.course = course
            a.type = '申请'
            a.save()
            return JsonResponse({'status': 'ok', 'msg': '申请成功，请等待审核'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '已申请该课程，请不要重复操作'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '申请失败，请检查后重试'})


@login_decorator
def user_exitcourse(request):
    user_exitcourse_form = UserExitCourseForm(request.POST)
    if user_exitcourse_form.is_valid():
        course_id = user_exitcourse_form.cleaned_data['course_id']
        reason = user_exitcourse_form.cleaned_data['reason']
        course = ScourseInfo.objects.filter(id=int(course_id), type='已选', student=request.user)[0]
        if course:
            course.type = '退选'
            course.reason = reason
            course.save()
            return JsonResponse({'status': 'ok', 'msg': '申请退选成功，请等待审核'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '课程错误，请稍后重试'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '未知错误，请稍后重试'})
