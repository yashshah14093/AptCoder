# Generated by Django 3.1 on 2020-10-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=10)),
            ],
        ),
    ]