# -*- coding: utf-8 -*-
# time:2023/4/25 9:08
# file rango_template_tags.py
# outhor:czy
# email:1060324818@qq.com
from django import template

from rango.models import Category
#这样也是可以的，不要去管报错
register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),'act_cat': cat}
