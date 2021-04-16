# Generated by Django 3.1.5 on 2021-01-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('year_in_school', models.CharField(choices=[('Technology Entrepreneurship', 'Technology Entrepreneurship'), ('Intro to Aerospace Structures', 'Intro to Aerospace Structures'), ('Connected Strategy', 'Connected Strategy'), ('Exercising Leadership', 'Exercising Leadership'), ('Intro to Project Management', 'Intro to Project Management'), ('Science of Happiness at Work', 'Science of Happiness at Work')], default='Technology Entrepreneurship', max_length=50)),
            ],
        ),
    ]