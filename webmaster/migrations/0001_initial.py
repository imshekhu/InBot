# Generated by Django 3.0.7 on 2020-07-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('frequencyfollow', models.IntegerField()),
                ('frequencyunfollow', models.IntegerField()),
                ('frequencypostcheck', models.IntegerField()),
                ('daysafterunfollow', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]