# Generated by Django 3.2.9 on 2022-01-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0002_auto_20220106_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='allbook',
        ),
        migrations.AddField(
            model_name='genre',
            name='allbook',
            field=models.ManyToManyField(to='ebook.Book'),
        ),
    ]