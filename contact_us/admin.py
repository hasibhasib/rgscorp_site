from django.contrib import admin
from .models import ContactForm

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')


admin.site.register(ContactForm, ContactFormAdmin)