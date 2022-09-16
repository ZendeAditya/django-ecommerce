from django.db import models

# Create your models here.
CATEGORY_TAGS = [
    ('laptops','laptops'),
    ('mobiles','mobiles'),
    ('shirts','shirts')
]
class Category(models.Model):
    categroy_name = models.CharField( max_length=150)
    category_desc = models.TextField()
    categroy_img = models.ImageField(upload_to='static/images/category_img/')
    category_tag = models.CharField(choices=CATEGORY_TAGS, max_length=7)


    def __str__(self):
        return self.categroy_name