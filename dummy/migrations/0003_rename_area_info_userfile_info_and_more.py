# Generated by Django 5.0.6 on 2024-07-18 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0002_alter_project_garden_alter_project_temple_mapfile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfile',
            old_name='area_info',
            new_name='info',
        ),
        migrations.RemoveField(
            model_name='userfile',
            name='avg_value',
        ),
    ]
