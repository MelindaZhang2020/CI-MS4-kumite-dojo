# Generated by Django 3.2.8 on 2021-10-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_banner_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='tag',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
