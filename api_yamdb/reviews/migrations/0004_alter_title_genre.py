# Generated by Django 3.2 on 2022-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221214_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genres', to='reviews.Genre', verbose_name='Жанры'),
        ),
    ]
