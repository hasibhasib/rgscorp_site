# Generated by Django 3.0.5 on 2020-04-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200408_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_picture_2',
            field=models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_3',
            field=models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_4',
            field=models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_main',
            field=models.ImageField(default='static/default_pro_pic.jpg', upload_to='pics'),
        ),
    ]