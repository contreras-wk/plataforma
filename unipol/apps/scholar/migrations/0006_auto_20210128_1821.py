# Generated by Django 3.1.5 on 2021-01-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0005_auto_20210128_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='present',
            field=models.BooleanField(default=False, help_text='Entry assistence'),
        ),
    ]
