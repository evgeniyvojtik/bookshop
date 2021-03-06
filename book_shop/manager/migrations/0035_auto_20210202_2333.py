# Generated by Django 3.1.5 on 2021-02-02 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0034_auto_20210127_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMPBook',
            fields=[
                ('title', models.CharField(max_length=250)),
                ('date', models.DateTimeField(null=True, verbose_name='date-time')),
                ('description', models.TextField(null=True, verbose_name='описание')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('genres', models.CharField(max_length=50, null=True, verbose_name='жанр')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('users_counted_stars', models.PositiveIntegerField(default=0, verbose_name='counted_stars')),
                ('count_users', models.PositiveIntegerField(default=0, verbose_name='counted_users')),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('authors', models.ManyToManyField(related_name='books_tmp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tmp_comment', to='manager.tmpbook'),
        ),
        migrations.AddField(
            model_name='usersrating',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_rate', to='manager.tmpbook'),
        ),
    ]
