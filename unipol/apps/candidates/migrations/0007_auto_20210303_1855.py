# Generated by Django 3.1.6 on 2021-03-04 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20210303_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='birth_certificate',
            new_name='file_birth_certificate',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='curp',
            new_name='file_curp',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='ine',
            new_name='file_ine',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='proof_of_address',
            new_name='file_proof_address',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='proof_of_courses',
            new_name='file_proof_courses',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='proof_of_studies',
            new_name='file_proof_studies',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='rfc',
            new_name='file_rfc',
        ),
    ]