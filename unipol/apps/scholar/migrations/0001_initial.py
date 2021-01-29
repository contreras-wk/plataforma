# Generated by Django 3.1.5 on 2021-01-27 23:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('hour', models.TimeField(default=django.utils.timezone.now)),
                ('present', models.DateField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='ScholarCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='ScholarCourseSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_theoretical', models.IntegerField(default=None)),
                ('evaluation_practice', models.IntegerField(default=None)),
                ('scholarcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholar.scholarcourse')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
        migrations.AddField(
            model_name='scholarcourse',
            name='qualifications',
            field=models.ManyToManyField(through='scholar.ScholarCourseSubject', to='course.Subject'),
        ),
        migrations.AddField(
            model_name='scholarcourse',
            name='scholar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholar.scholar'),
        ),
        migrations.AddField(
            model_name='scholar',
            name='courses',
            field=models.ManyToManyField(through='scholar.ScholarCourse', to='course.Course'),
        ),
    ]