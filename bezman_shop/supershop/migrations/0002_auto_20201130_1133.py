# Generated by Django 3.1.3 on 2020-11-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supershop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
