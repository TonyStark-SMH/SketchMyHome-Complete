# Generated by Django 5.0.6 on 2024-07-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0008_userfile_delete_userpng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='dxf_file',
            field=models.FileField(blank=True, null=True, upload_to='dxfs/'),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='png_image',
            field=models.ImageField(blank=True, null=True, upload_to='pngs/'),
        ),
    ]