# Generated by Django 3.0.6 on 2020-07-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('is_followed_ever', models.BooleanField(default=False)),
                ('is_unfollowed', models.BooleanField(default=False)),
                ('followed_at', models.DateTimeField()),
                ('unfollowed_at', models.DateTimeField()),
            ],
        ),
    ]
