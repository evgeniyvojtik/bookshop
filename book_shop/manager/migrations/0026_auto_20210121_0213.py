# Generated by Django 3.1.5 on 2021-01-20 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0025_auto_20210121_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_rate', to=settings.AUTH_USER_MODEL),
        ),
    ]
