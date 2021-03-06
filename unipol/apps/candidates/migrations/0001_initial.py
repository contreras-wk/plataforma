# Generated by Django 3.1.5 on 2021-01-27 23:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(help_text='Entry CURP', max_length=19, unique=True)),
                ('rfc', models.CharField(help_text='Entry RFC', max_length=13, unique=True)),
                ('name', models.CharField(help_text='Entry name', max_length=50)),
                ('last_name', models.CharField(help_text='Entry last name', max_length=50)),
                ('mothers_last_name', models.CharField(help_text='Entry mothers last name', max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], help_text='Entry gender', max_length=1)),
                ('age', models.IntegerField(help_text='Entry age')),
                ('height', models.IntegerField(help_text='Entry height')),
                ('belongs_other_corporation', models.BooleanField(default=False)),
                ('date_crate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Candidate',
            },
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_studies', models.CharField(help_text='Entry level study', max_length=15)),
                ('details', models.CharField(help_text='Entry details level study', max_length=60, null=True)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
            options={
                'verbose_name': 'Studie',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_certificate', models.FileField(upload_to='documents')),
                ('curp', models.FileField(upload_to='documents')),
                ('rfc', models.FileField(upload_to='documents')),
                ('ine', models.FileField(upload_to='documents')),
                ('proof_of_address', models.FileField(upload_to='documents')),
                ('proof_of_studies', models.FileField(upload_to='documents')),
                ('proof_of_courses', models.FileField(blank=True, null=True, upload_to='documents')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
            options={
                'verbose_name': 'Document',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_residence', models.CharField(max_length=35)),
                ('delegacion', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('street', models.CharField(max_length=50)),
                ('num_outdoor', models.IntegerField()),
                ('num_inside', models.IntegerField(null=True)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
            options={
                'verbose_name': 'Direction',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(help_text='Entry Telephone', max_length=10)),
                ('mobile_telephone', models.CharField(blank=True, help_text='Entry Mobile Telephone', max_length=10, null=True)),
                ('email', models.EmailField(help_text='Entry Email', max_length=254, unique=True)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='CallInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.TextField()),
                ('attraction', models.TextField()),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
            options={
                'verbose_name': 'Call_Info',
            },
        ),
    ]
