# -*- coding: utf-8 -*-
# time:2023/4/23 18:28
# file urls.py
# outhor:czy
# email:1060324818@qq.com
# <!-- {% load staticfiles %} 告诉django使用静态文件 但即使不用这个也可以显示，用了fang-->
"""    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^restricted/', views.restricted, name='restricted'),
    <!--<li><a href="{% url 'restricted' %}">Restricted Page</a></li>>-->
    """
from django.urls import re_path, path, include
from . import views
#用rango的时候爆红，用了点之后就没有了
urlpatterns = [
    re_path(r'^adout/', views.adout, name='adout'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add_category/$', views.add_category, name='add_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page, name='add_page'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name='show_category'),
    re_path(r'^restricted/', views.restricted, name='restricted'),
    re_path(r'^goto/$', views.track_url, name='goto'),
    re_path(r'^register_profile/$', views.register_profile, name='register_profile'),
    re_path(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    re_path(r'^profiles/$', views.list_profiles, name='list_profiles'),
    re_path(r'^like/$', views.like_category, name='like_category'),
    re_path(r'^suggest/$', views.suggest_category, name='suggest_category'),
]
#之前爆红的一次是因为path里面用正则会报错
#终于平出来了，原来是adout平戳了

#相对路径的时候rango.views.adout行不通
#{% url 'show_category' category.slug %} 这样也不行

