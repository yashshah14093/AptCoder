# Generated by Django 3.1 on 2020-10-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_teachercourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=1500)),
            ],
        ),
    ]