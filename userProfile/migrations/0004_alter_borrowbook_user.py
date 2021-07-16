# Generated by Django 3.2.5 on 2021-07-15 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userProfile', '0003_auto_20210715_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
