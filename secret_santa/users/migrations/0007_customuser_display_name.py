# Generated by Django 3.1.6 on 2021-03-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_customuser_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(default='Anonymous', max_length=20),
            preserve_default=False,
        ),
    ]