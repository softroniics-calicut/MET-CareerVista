# Generated by Django 4.2.7 on 2024-01-03 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='job_id',
            new_name='job',
        ),
    ]
