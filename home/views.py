
from django.shortcuts import render
from category.models import Category
from products.models import Products
# Create your views here.
def home(request):
    category = Category.objects.all()
    products = Products.objects.all()[:12]
    laptops = Products.objects.filter(prodcut_category__categroy_name="laptops")
    mobile = Products.objects.filter(prodcut_category__categroy_name="Mobiles")
    shirt = Products.objects.filter(prodcut_category__categroy_name="Shirts")
    context = {
        'category':category,
        'products':products,
        'laptops':laptops,
        'mobiles':mobile,
        'shirts':shirt
        }
    print(mobile)
    print(shirt)
    return render(request,'index.html',context)


def prodcut_view(request,product_name):
    product = Products.objects.filter(product_name=product_name)
    print('product',product)
    context = {'product':product}
    return render(request,'products\productDetails.html',context)

def category_view(request,prodcut_category__categroy_name):
    context={
        'name':prodcut_category__categroy_name
    }
    return render(request,'category/cat.html',context)