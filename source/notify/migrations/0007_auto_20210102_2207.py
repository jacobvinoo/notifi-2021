# Generated by Django 3.1.3 on 2021-01-02 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0006_auto_20210102_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.employee'),
        ),
    ]
