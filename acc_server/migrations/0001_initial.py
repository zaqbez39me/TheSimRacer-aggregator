# Generated by Django 3.1.7 on 2021-02-27 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('starts_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventSettings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pre_race_waiting_time_seconds', models.IntegerField(default=60)),
                ('session_over_time_seconds', models.IntegerField(default=120)),
                ('ambient_temp', models.IntegerField(default=26)),
                ('track_temp', models.IntegerField(default=26)),
                ('cloud_level', models.FloatField(default=0)),
                ('weather_randomness', models.IntegerField(default=0)),
                ('post_qualy_seconds', models.IntegerField(default=0)),
                ('post_race_seconds', models.IntegerField(default=0)),
                ('meta_data', models.TextField(default='')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acc_server.event')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('unique_pit_boxes', models.IntegerField()),
                ('private_server_slots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hour_of_day', models.IntegerField(default=8)),
                ('day_of_weekend', models.IntegerField(default=1)),
                ('time_multiplier', models.IntegerField(default=0)),
                ('session_type', models.IntegerField(default=0)),
                ('session_duration_minutes', models.IntegerField()),
                ('event_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc_server.eventsettings')),
            ],
        ),
        migrations.CreateModel(
            name='ServerSettings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('server_name', models.CharField(max_length=255)),
                ('admin_password', models.CharField(max_length=255)),
                ('car_group', models.CharField(default='FreeForAll', max_length=50)),
                ('track_medals_requirement', models.IntegerField(default=0)),
                ('safety_rating_requirement', models.IntegerField(default=-1)),
                ('password', models.CharField(default='', max_length=255)),
                ('spectator_password', models.CharField(default='', max_length=255)),
                ('max_car_slots', models.IntegerField(default=64)),
                ('dump_leaderboards', models.IntegerField(default=1)),
                ('is_race_locked', models.IntegerField(default=1)),
                ('randomize_track_when_empty', models.IntegerField(default=1)),
                ('allow_auto_dq', models.IntegerField(default=0)),
                ('short_formation_lap', models.IntegerField(default=0)),
                ('dump_entry_list', models.IntegerField(default=1)),
                ('formation_lap_type', models.IntegerField(default=3)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acc_server.event')),
            ],
        ),
        migrations.CreateModel(
            name='ServerConfig',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('udp_port', models.IntegerField(default=0, unique=True)),
                ('tcp_port', models.IntegerField(default=0, unique=True)),
                ('max_connections', models.IntegerField(default=100)),
                ('lan_discovery', models.IntegerField(default=0)),
                ('register_to_lobby', models.IntegerField(default=1)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acc_server.event')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='eventsettings',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc_server.track'),
        ),
        migrations.CreateModel(
            name='EventRules',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('qualify_standing_type', models.IntegerField(default=-1)),
                ('pit_window_length_sec', models.IntegerField(default=-1)),
                ('driver_stint_time_sec', models.IntegerField(default=-1)),
                ('mandatory_pitstop_count', models.IntegerField(default=0)),
                ('max_total_driving_time', models.IntegerField(default=-1)),
                ('max_drivers_count', models.IntegerField()),
                ('is_refuelling_allowed_in_race', models.BooleanField(default=True)),
                ('is_refuelling_time_fixed', models.BooleanField(default=False)),
                ('is_mandatory_pitstop_refuelling_required', models.BooleanField(default=False)),
                ('is_mandatory_pitstop_tyre_change_required', models.BooleanField(default=False)),
                ('is_mandatory_pitstop_swap_driver_required', models.BooleanField(default=False)),
                ('tyre_set_count', models.IntegerField(default=50)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acc_server.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc_server.playlist'),
        ),
        migrations.CreateModel(
            name='AssistRules',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stability_control_level_max', models.IntegerField(default=100)),
                ('disable_autosteer', models.BooleanField(default=True)),
                ('disable_auto_lights', models.BooleanField(default=False)),
                ('disable_auto_wiper', models.BooleanField(default=False)),
                ('disable_auto_engine_start', models.BooleanField(default=False)),
                ('disable_auto_pit_limiter', models.BooleanField(default=False)),
                ('disable_auto_gear', models.BooleanField(default=False)),
                ('disable_auto_clutch', models.BooleanField(default=False)),
                ('disable_auto_line', models.BooleanField(default=False)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acc_server.event')),
            ],
        ),
    ]
