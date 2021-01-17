# Generated by Django 3.1.5 on 2021-01-17 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0020_book_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(verbose_name='rating')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.book', verbose_name='users_rate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='book_rate')),
            ],
            options={
                'unique_together': {('book', 'user')},
            },
        ),
    ]