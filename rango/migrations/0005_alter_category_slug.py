# Generated by Django 4.2 on 2023-04-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_alter_category_options_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
