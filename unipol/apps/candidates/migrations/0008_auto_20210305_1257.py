# Generated by Django 3.1.6 on 2021-03-05 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0007_auto_20210303_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='date_crate',
            new_name='date_create',
        ),
    ]