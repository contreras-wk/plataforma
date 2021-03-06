# Generated by Django 3.1.5 on 2021-02-03 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0007_auto_20210128_1826'),
        ('initial_training', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Initial_Training',
            new_name='InitialTraining',
        ),
        migrations.CreateModel(
            name='AcademicPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_test_academic', models.DateField()),
                ('status_test_academic', models.BooleanField()),
                ('initial_training', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='initial_training.initialtraining')),
            ],
        ),
    ]
