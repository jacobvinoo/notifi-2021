# Generated by Django 3.1.3 on 2021-01-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0015_auto_20210109_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='notification',
        ),
        migrations.AddField(
            model_name='work',
            name='notification',
            field=models.ManyToManyField(to='notify.Notification'),
        ),
    ]
