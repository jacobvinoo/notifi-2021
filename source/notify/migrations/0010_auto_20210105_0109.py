# Generated by Django 3.1.3 on 2021-01-05 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0009_auto_20210103_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='destination_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to='notify.company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_admin',
            field=models.BooleanField(blank=True, default='False'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.employee'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='origin_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.company'),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.company')),
            ],
        ),
        migrations.AlterField(
            model_name='notification',
            name='service_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.services'),
        ),
    ]
