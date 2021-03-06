# Generated by Django 3.1.3 on 2021-01-01 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0003_notification_service_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
