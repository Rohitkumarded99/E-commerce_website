# Generated by Django 3.0.7 on 2020-07-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200723_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=500),
        ),
    ]
