# Generated by Django 3.2 on 2022-12-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221217_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='review_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='review_id',
            field=models.ForeignKey(db_column='review_id', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(db_column='title_id', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Произведение'),
        ),
    ]
