# Generated by Django 3.2.7 on 2021-10-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_rating'),
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='products.Variation'),
        ),
    ]
