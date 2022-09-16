from itertools import product
from django.contrib import admin
from .models import Products
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','product_discount_price','prodcut_size','product_img']

admin.site.register(Products,ProductAdmin)