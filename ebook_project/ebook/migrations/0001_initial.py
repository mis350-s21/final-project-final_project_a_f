# Generated by Django 3.2.9 on 2022-01-06 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=10)),
                ('inventory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=8, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('credit_card', models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('allbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebook.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebook.genra'),
        ),
    ]
