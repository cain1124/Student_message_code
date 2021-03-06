from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile, EmailVerifyCode
from behavior.models import ScourseInfo


class UserRegisterForm(forms.Form):
    xh = forms.CharField(max_length=10, required=True, min_length=10, error_messages={
        'required': '请填写学号',
        'min_length': '请输入规范学号',
        'max_length': '请输入规范学号'
    })
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=6, max_length=15, required=True, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位'
    })
    captcha = CaptchaField()


class UserLoginForm(forms.Form):
    xh = forms.CharField(max_length=10, required=True, min_length=10, error_messages={
        'required': '请填写学号',
        'min_length': '请输入规范学号',
        'max_length': '请输入规范学号'
    })
    password = forms.CharField(required=True, min_length=6, max_length=15, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位',
    })
    # captcha = CaptchaField(


class UserForgetForm(forms.Form):
    email = forms.EmailField(required=True)


class UserResetForm(forms.Form):
    password = forms.CharField(min_length=6, max_length=15, required=True, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位'
    })
    password1 = forms.CharField(min_length=6, max_length=15, required=True, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位'
    })
    captcha = CaptchaField()


class UserChangeImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserChangeEmailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']


class UserResetEmailForm(forms.ModelForm):
    class Meta:
        model = EmailVerifyCode
        fields = ['email', 'code']


class UserChangePwdForm(forms.Form):
    password = forms.CharField(min_length=6, max_length=15, required=True, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位'
    })
    password1 = forms.CharField(min_length=6, max_length=15, required=True, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得少于6位',
        'max_length': '密码不得超过15位'
    })


class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']


class UserExitCourseForm(forms.Form):
    reason = forms.CharField(max_length=200, required=True, error_messages={
        'required': '请填写原因',
        'max_length': '原因不得超过200位'
    })
    course_id = forms.CharField(required=True, max_length=20)
