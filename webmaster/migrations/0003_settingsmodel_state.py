# Generated by Django 3.0.7 on 2020-07-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmaster', '0002_targetmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsmodel',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
