# Generated by Django 2.1.7 on 2019-03-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190328_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_banner_image',
            field=models.ImageField(default='', upload_to='./banner'),
        ),
    ]
