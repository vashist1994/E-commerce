# Generated by Django 2.1.7 on 2019-03-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190327_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(default='', upload_to='shop/static/shop/img/'),
        ),
    ]