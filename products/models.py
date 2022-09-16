from django.db import models
from category.models import Category
# Create your models here.

class Products(models.Model):
    prodcut_category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_desc = models.TextField()
    product_price = models.PositiveIntegerField()
    product_discount_price = models.PositiveIntegerField()
    product_img = models.ImageField(upload_to='static/images/prodcutImages/')
    prodcut_size = models.CharField(null=True, blank=True, max_length=50)


    def __str__(self):
        return self.product_name