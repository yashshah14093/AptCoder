# Generated by Django 3.1 on 2020-10-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='serialNo',
        ),
    ]
