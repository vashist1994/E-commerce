# Generated by Django 2.1.7 on 2019-03-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190327_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(default='', upload_to='shop/img'),
        ),
    ]