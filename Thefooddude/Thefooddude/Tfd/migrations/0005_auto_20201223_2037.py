# Generated by Django 3.1.3 on 2020-12-23 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tfd', '0004_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='res_id',
            new_name='restaurant',
        ),
    ]
