# Generated by Django 3.2 on 2022-01-25 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220111_2044'),
        ('order', '0015_auto_20220125_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='box_ordered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.box'),
        ),
    ]
