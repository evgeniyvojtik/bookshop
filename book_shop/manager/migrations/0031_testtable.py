# Generated by Django 3.1.5 on 2021-01-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_auto_20210124_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
