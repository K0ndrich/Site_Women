# Generated by Django 5.0.3 on 2024-03-13 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_husband_women_hasband'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='hasband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wumam', to='women.husband'),
        ),
    ]
