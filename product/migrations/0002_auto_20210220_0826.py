# Generated by Django 3.1.6 on 2021-02-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='productimage/', verbose_name='Фото товара'),
        ),
    ]
