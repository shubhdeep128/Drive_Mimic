# Generated by Django 2.2.2 on 2019-06-16 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20190616_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
