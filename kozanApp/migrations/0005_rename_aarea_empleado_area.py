# Generated by Django 4.1 on 2022-12-03 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kozanApp', '0004_alter_area_options_alter_area_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='aarea',
            new_name='area',
        ),
    ]
