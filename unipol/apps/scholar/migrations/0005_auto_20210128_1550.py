# Generated by Django 3.1.5 on 2021-01-28 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210128_1550'),
        ('candidates', '0002_auto_20210128_0842'),
        ('scholar', '0004_scholarcoursesubject_assistances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='present',
            field=models.DateField(default=False, help_text='Entry assistence'),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='candidate',
            field=models.OneToOneField(help_text='Entry candidates scholar', on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate'),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='courses',
            field=models.ManyToManyField(help_text='Entry courses scholar', through='scholar.ScholarCourse', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='scholarcourse',
            name='status',
            field=models.BooleanField(default=False, help_text='Entry status scholar course'),
        ),
    ]