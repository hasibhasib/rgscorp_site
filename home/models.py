from django.db import models


class HeaderImage(models.Model):
    header_image = models.ImageField(upload_to='pics')
