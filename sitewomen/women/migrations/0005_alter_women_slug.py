# Generated by Django 5.0.3 on 2024-03-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
