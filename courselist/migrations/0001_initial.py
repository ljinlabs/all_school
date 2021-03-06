# Generated by Django 3.0.4 on 2020-08-27 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(choices=[('fa', 'Fall'), ('sp', 'Spring'), ('su', 'Summer')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=20)),
                ('course_lectures', models.URLField()),
                ('course_forums', models.URLField()),
                ('course_homework', models.URLField()),
                ('course_labs', models.URLField()),
                ('course_last_updated', models.DateTimeField(auto_now=True)),
                ('course_created', models.DateTimeField(auto_now_add=True)),
                ('course_semester', models.CharField(choices=[('fa-2020', 'Fall 2020'), ('sp-2021', 'Spring 2021'), ('su-2021', 'Summer 2021')], max_length=10)),
                ('course_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courselist.Semester')),
            ],
        ),
    ]
