# Generated by Django 3.2 on 2022-12-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20221220_0936'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]