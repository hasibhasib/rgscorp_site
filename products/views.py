from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Products, ProductCategory


def products(request):
    product_list = Products.objects.all()
    p_category = ProductCategory.objects.all()
    return render(request, 'all_products.html', {'p_categories': p_category, 'product_list': product_list})


def products_details(request, slug):
    product_list = Products.objects.all()
    detail_product = Products.objects.get(slug=slug)
    category = detail_product.product_category
    similar_category = product_list.filter(product_category=category)
    p_category = ProductCategory.objects.all()
    return render(request, 'product_description.html', {'p_categories': p_category, 'detail_product': detail_product,
                                                        'product_list': product_list,
                                                        'similar_category': similar_category})


def list_of_post_category(request, slug):
    categories = ProductCategory.objects.all()
    products_all = Products.objects.all()

    category = get_object_or_404(ProductCategory, slug=slug)
    product = products_all.filter(product_category=category)
    return render(request, 'p_category.html', {'categories': categories, 'c_product': product, 'category': category,
                                               'products_all': products_all})
