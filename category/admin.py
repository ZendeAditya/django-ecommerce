from django.contrib import admin

from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','categroy_name','categroy_img']

admin.site.register(Category,CategoryAdmin)