from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products'),
    path('<slug:slug>', views.products_details, name='product_detail'),
    path('category/<slug:slug>', views.list_of_post_category, name='category_list'),
]