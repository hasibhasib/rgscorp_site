# Generated by Django 3.0.5 on 2020-04-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200408_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandname',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=60), max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=60), max_length=250, unique=True),
        ),
    ]
