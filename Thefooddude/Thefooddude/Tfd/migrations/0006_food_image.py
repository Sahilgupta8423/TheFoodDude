# Generated by Django 3.1.3 on 2020-12-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tfd', '0005_auto_20201223_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default='', upload_to='Tfd/images'),
        ),
    ]
