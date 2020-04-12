from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=250, unique=True, default=category_name)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('product:list_of_post_category', args=[self.slug])

    def __str__(self):
        return self.category_name


class BrandName(models.Model):
    brand_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=250, unique=True, default=brand_name)

    class Meta:
        ordering = ('brand_name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=250, unique=True, default=product_name)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_brand = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    product_picture_main = models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics')
    product_picture_2 = models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics')
    product_picture_3 = models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics')
    product_picture_4 = models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics')
    product_specification = models.TextField(default='No Specification Available')
    product_accessories = models.TextField(default='No Accessories Available')
    product_other_description = models.TextField(default='No Description Available')
    optional_accessories = models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics')

