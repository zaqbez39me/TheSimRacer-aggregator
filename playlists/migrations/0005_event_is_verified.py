# Generated by Django 3.1.7 on 2021-04-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0004_auto_20210402_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
