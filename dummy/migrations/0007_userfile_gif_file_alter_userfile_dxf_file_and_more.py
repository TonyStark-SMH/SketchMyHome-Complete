# Generated by Django 5.0.6 on 2024-08-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0006_alter_userfile_dxf_file_alter_userfile_png_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='gif_file',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='dxf_file',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='png_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
