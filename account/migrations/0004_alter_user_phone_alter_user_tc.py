# Generated by Django 5.0.6 on 2024-10-22 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='0000000000', max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^\\d{10}$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tc',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
