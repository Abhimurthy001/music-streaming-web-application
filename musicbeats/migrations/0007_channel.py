# Generated by Django 3.0.8 on 2020-08-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0006_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=100000000)),
            ],
        ),
    ]
