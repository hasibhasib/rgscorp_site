from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=250, default=0)
    email = models.EmailField()
    subject = models.CharField(max_length=500, default=0)
    message = models.TextField(max_length=3000, default=0)
