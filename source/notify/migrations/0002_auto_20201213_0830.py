# Generated by Django 3.1.3 on 2020-12-13 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_outage', models.DateField()),
                ('window_start_time', models.TimeField()),
                ('window_end_time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orgin_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.company')),
            ],
        ),
    ]
