# Generated by Django 4.1 on 2022-08-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalwallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
    ]