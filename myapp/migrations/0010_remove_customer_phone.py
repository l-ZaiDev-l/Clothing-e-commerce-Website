# Generated by Django 4.1.7 on 2023-06-25 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_customer_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
