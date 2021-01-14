# Generated by Django 3.1.3 on 2021-01-09 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0014_auto_20210109_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='destination_company',
        ),
        migrations.AddField(
            model_name='notification',
            name='destination_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to='notify.company'),
        ),
    ]