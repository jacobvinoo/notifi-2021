# Generated by Django 3.1.3 on 2021-01-01 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0004_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
    ]
