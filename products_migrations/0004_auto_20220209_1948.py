# Generated by Django 3.2 on 2022-02-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_box_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product_on_box',
            name='product',
        ),
        migrations.AddField(
            model_name='product_on_box',
            name='product',
            field=models.ManyToManyField(related_name='product', to='products.Product'),
        ),
    ]
