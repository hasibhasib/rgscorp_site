from django.contrib import admin
from .models import ProductCategory, BrandName, Products


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')


admin.site.register(ProductCategory, ProductCategoryAdmin)


class BrandNameAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'slug')


admin.site.register(BrandName)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'product_brand')


admin.site.register(Products, ProductAdmin)
