# Generated by Django 5.0.3 on 2024-03-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_alter_women_husband'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
