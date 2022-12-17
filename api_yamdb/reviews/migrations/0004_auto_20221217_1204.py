# Generated by Django 3.2 on 2022-12-17 12:04

import django.core.validators
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221217_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Оценка должна быть не меньше 1.'), django.core.validators.MaxValueValidator(10, 'Оценка должна быть не больше 10.')], verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genres',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='titles', through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Год выхода'),
        ),
    ]
