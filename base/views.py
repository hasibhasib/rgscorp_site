from django.shortcuts import render
from django.http import HttpResponse
from .models import HeaderImage
from products.models import Products, ProductCategory


def base(request):
    p_category = ProductCategory.objects.all()
    return render(request, 'base.html', {'p_categories': p_category})
