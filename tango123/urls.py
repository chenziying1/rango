"""tango123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

from tango123.rango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$', views.index, name='index')
]
"""
from django.conf.urls.static import static

from . import settings
from django.urls import path, re_path, reverse
from django.contrib import admin
from django.urls import include
from rango import views
from registration.backends.simple.views import RegistrationView
# 定义一个类
# 用户成功注册后重定向到首页
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

#终于解决了这个报错，不要去理会就好
urlpatterns = [
    re_path(r'^accounts/register/$',MyRegistrationView.as_view(),name='registration_register'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^rango/', include('rango.urls')),
    path('rango/adout', include('rango.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    # 上面的映射把以 rango/ 开头的 URL 交给 rango 应用处理
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#!!!!这里的报错居然是因为我import 错了！
