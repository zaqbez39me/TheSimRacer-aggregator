# Generated by Django 3.1.8 on 2021-05-21 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0009_playlist_grid_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='team',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
