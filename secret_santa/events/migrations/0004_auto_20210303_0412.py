# Generated by Django 3.1.6 on 2021-03-03 04:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='time',
        ),
        migrations.AddField(
            model_name='events',
            name='game_length',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(60)]),
            preserve_default=False,
        ),
    ]
