# Generated by Django 3.0.7 on 2020-07-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmaster', '0004_auto_20200720_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmodel',
            name='frequencypostcheck',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
