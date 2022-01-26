# Generated by Django 3.2 on 2022-01-26 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0016_order_box_ordered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderbox',
            options={'verbose_name_plural': 'Ordered boxes'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='box_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
