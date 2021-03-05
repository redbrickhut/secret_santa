# Generated by Django 3.1.6 on 2021-03-02 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_pictures')),
                ('time', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('revealed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts', related_query_name='gifts', to='events.events')),
            ],
        ),
    ]
