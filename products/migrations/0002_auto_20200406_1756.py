# Generated by Django 3.0.5 on 2020-04-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='optional_accessories',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='product_accessories',
            field=models.TextField(default='...'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_other_description',
            field=models.TextField(default='...'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_picture_3',
            field=models.ImageField(default=0, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_picture_4',
            field=models.ImageField(default=0, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_specification',
            field=models.TextField(default='...'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_brand',
            field=models.CharField(max_length=60, verbose_name='<django.db.models.query_utils.DeferredAttribute object at 0x04554328>'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(max_length=60, verbose_name='<django.db.models.query_utils.DeferredAttribute object at 0x04554820>'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_2',
            field=models.ImageField(default=0, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture_main',
            field=models.ImageField(default='default_pro_pic.jpg', upload_to='pics'),
        ),
    ]
