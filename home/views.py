from django.shortcuts import render
from django.http import HttpResponse
from .models import HeaderImage
from products.models import Products, ProductCategory


def home(request):
    p_category = ProductCategory.objects.all()
    products = Products.objects.all()
    return render(request, 'index.html', {'p_categories': p_category, 'products': products})

