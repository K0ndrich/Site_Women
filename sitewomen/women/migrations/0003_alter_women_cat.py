# Generated by Django 5.0.3 on 2024-03-12 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_category_women_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category'),
        ),
    ]
