# Generated by Django 4.1.7 on 2023-06-01 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]
