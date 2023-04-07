from csv import list_dialects
from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

# 맨위 상단 이름 변경
admin.site.site_header = '신사무 관리 시스템 페이지'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ['category']



admin.site.register(Product, ProductAdmin)
# admin.site.unregister(Group)  # Group 기능 제거할수 있는 방법
