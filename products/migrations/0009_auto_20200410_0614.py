# Generated by Django 3.0.5 on 2020-04-10 00:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200408_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_other_description',
            field=tinymce.models.HTMLField(default='No Description Available'),
        ),
    ]