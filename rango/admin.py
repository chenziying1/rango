from django.contrib import admin
from .models import Category,Page
from .models import UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
# 添加这个类，定制管理界面
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# 注册定制界面的类
"""admin.site.register(Category, CategoryAdmin)"""

