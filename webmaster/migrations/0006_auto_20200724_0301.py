# Generated by Django 3.0.7 on 2020-07-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmaster', '0005_auto_20200721_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsmodel',
            name='suspicion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='suspicioncode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
