# -*- coding: utf-8 -*-
# time:2023/4/24 10:07
# file populate_rango.py
# outhor:czy
# email:1060324818@qq.com

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango123.settings')

import django
django.setup()
from rango.models import Category,Page

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views  = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if c.name == "Python":
        c.views = 128
        c.likes = 64
    if c.name == "Django":
        c.views = 64
        c.likes = 32
    if c.name == "Other Frameworks":
        c.views = 32
        c.likes = 16
    c.save()
    return c

def populate():
    python_pages = [
                    {"title": "Official Python Tutorial",
                    "url":"http://docs.python.org/2/tutorial/"},

                    {"title": "How to Think like a Computer Scientist",
                        "url": "http://www.greenteapress.com/thinkpython/"},

                    {"title": "Learn Python in 10 Minutes",
                    "url": "http://www.korokithakis.net/tutorials/python/"}
                     ]

    django_pages = [
                    {"title": "Official Django Tutorial",
                    "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},

                    {"title": "Django Rocks",
                    "url": "http://www.djangorocks.com/"},

                    {"title": "How to Tango with Django",
                    "url": "http://www.tangowithdjango.com/"}
                    ]


    other_pages = [
                    {"title": "Bottle",
                    "url":"http://bottlepy.org/docs/dev/"},

                    {"title": "Flask",
                    "url": "http://flask.pocoo.org"}
                ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],10)

    # 打印添加的分类
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()