"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .views import user_login, user_register, user_forget, user_logout, user_reset, user_info, user_changeimage, \
    user_changeemail, user_resetemail, user_changepwd, user_time, user_msg, user_deletemsg, user_course, user_grade, \
    user_changeinfo, user_choosecourse, user_apply, user_exitcourse

urlpatterns = [
    url(r'^user_register/$', user_register, name='user_register'),
    url(r'^user_login/$', user_login, name='user_login'),
    url(r'^user_logout/$', user_logout, name='user_logout'),
    url(r'^user_forget/$', user_forget, name='user_forget'),
    url(r'^user_reset/(\w+)/$', user_reset, name='user_reset'),
    url(r'user_info/$', user_info, name='user_info'),
    url(r'^user_changeimage/$', user_changeimage, name='user_changeimage'),
    url(r'^user_changeemail/$', user_changeemail, name='user_changeemail'),
    url(r'^user_resetemail/$', user_resetemail, name='user_resetemail'),
    url(r'^user_changepwd/$', user_changepwd, name='user_changepwd'),
    url(r'^user_time/$', user_time, name='user_time'),
    url(r'^user_msg/$', user_msg, name='user_msg'),
    url(r'^user_deletemsg/$', user_deletemsg, name='user_deletemsg'),
    url(r'^user_course/$', user_course, name='user_course'),
    url(r'^user_grade/$', user_grade, name='user_grade'),
    url(r'^user_changeinfo/$', user_changeinfo, name='user_changeinfo'),
    url(r'^user_choosecourse/$', user_choosecourse, name='user_choosecourse'),
    url(r'^user_apply/$', user_apply, name='user_apply'),
    url(r'^user_exitcourse/$', user_exitcourse, name='user_exitcourse'),
]
