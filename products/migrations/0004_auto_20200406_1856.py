# Generated by Django 3.0.5 on 2020-04-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200406_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='optional_accessories',
            field=models.ImageField(default='default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_2',
            field=models.ImageField(default='default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_3',
            field=models.ImageField(default='default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_4',
            field=models.ImageField(default='default_pro_pic.jpg', upload_to='pics'),
        ),
    ]
