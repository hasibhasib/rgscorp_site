from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products, ProductCategory
from .models import ContactForm


def contact_us(request):
    p_category = ProductCategory.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactForm()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, 'contact.html', {'p_categories': p_category})

    return render(request, 'contact.html', {'p_categories': p_category})
