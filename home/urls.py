from django.urls import path 
from . import views


app_name='home'
urlpatterns = [
    path('',views.home,name='home'),
    path('prodcut-view/<str:product_name>/',views.prodcut_view,name='prodcut_view'),
    path('category/<str:prodcut_category__categroy_name>/',views.category_view,name='category_view')
]
