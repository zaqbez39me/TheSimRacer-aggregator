from django.db import models
from django.db.models import ForeignKey, IntegerField, CharField, BooleanField, FloatField, TextField, DateTimeField, OneToOneField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import signals


class Track(models.Model):

    name = CharField(max_length=100, null=False, unique=True)
    unique_pit_boxes = IntegerField(null=False)
    private_server_slots = IntegerField(null=False)


class EventSettings(models.Model):

    track = ForeignKey(Track, models.deletion.CASCADE, null=True)
    pre_race_waiting_time_seconds = IntegerField(default=60)
    session_over_time_seconds = IntegerField(default=120)
    ambient_temp = IntegerField(default=26)
    track_temp = IntegerField(default=26)
    cloud_level = FloatField(default=0)
    weather_randomness = IntegerField(default=0)
    post_qualy_seconds = IntegerField(default=0)
    post_race_seconds = IntegerField(default=0)
    meta_data = TextField(default="")


class Session(models.Model):

    hour_of_day = IntegerField(null=False, default=8)
    day_of_weekend = IntegerField(null=False, default=1)
    time_multiplier = IntegerField(null=False, default=0)
    session_type = IntegerField(null=False, default=0)
    session_duration_minutes = IntegerField(null=False)


class EventRules(models.Model):

    qualify_standing_type = IntegerField(null=False, default=-1)
    pit_window_length_sec = IntegerField(null=False, default=-1)
    driver_stint_time_sec = IntegerField(null=False, default=-1)
    mandatory_pitstop_count = IntegerField(null=False, default=0)
    max_total_driving_time = IntegerField(null=False, default=-1)
    max_drivers_count = IntegerField(null=False, default=100)
    is_refuelling_allowed_in_race = BooleanField(default=True)
    is_refuelling_time_fixed = BooleanField(default=False)
    is_mandatory_pitstop_refuelling_required = BooleanField(default=False)
    is_mandatory_pitstop_tyre_change_required = BooleanField(default=False)
    is_mandatory_pitstop_swap_driver_required = BooleanField(default=False)
    tyre_set_count = IntegerField(default=50)


class AssistRules(models.Model):

    stability_control_level_max = IntegerField(default=100)
    disable_autosteer = BooleanField(default=True)
    disable_auto_lights = BooleanField(default=False)
    disable_auto_wiper = BooleanField(default=False)
    disable_auto_engine_start = BooleanField(default=False)
    disable_auto_pit_limiter = BooleanField(default=False)
    disable_auto_gear = BooleanField(default=False)
    disable_auto_clutch = BooleanField(default=False)
    disable_auto_line = BooleanField(default=False)


class ServerSettings(models.Model):

    server_name = CharField(max_length=255)
    admin_password = CharField(max_length=255)
    car_group = CharField(max_length=50, default="FreeForAll")
    track_medals_requirement = IntegerField(default=0)
    safety_rating_requirement = IntegerField(default=-1)
    password = CharField(max_length=255, default="")
    spectator_password = CharField(max_length=255, default="")
    max_car_slots = IntegerField(default=64)
    dump_leaderboards = IntegerField(default=1)
    is_race_locked = IntegerField(default=1)
    randomize_track_when_empty = IntegerField(default=1)
    allow_auto_dq = IntegerField(default=0)
    short_formation_lap = IntegerField(default=0)
    dump_entry_list = IntegerField(default=1)
    formation_lap_type = IntegerField(default=3)


class ServerConfig(models.Model):

    udp_port = IntegerField(default=0)
    tcp_port = IntegerField(default=0)
    max_connections = IntegerField(default=100)
    lan_discovery = IntegerField(default=0)
    register_to_lobby = IntegerField(default=1)


class AccEvent(models.Model):

    server_settings = OneToOneField(ServerSettings, models.deletion.RESTRICT, null=True)
    server_config = OneToOneField(ServerConfig, models.deletion.RESTRICT, null=True)
    assist_rules = OneToOneField(AssistRules, models.deletion.RESTRICT, null=True)
    event_settings = OneToOneField(EventSettings, models.deletion.RESTRICT, null=True)
    event_rules = OneToOneField(EventRules, models.deletion.RESTRICT, null=True)


@receiver(signals.pre_save, sender=AccEvent)
def create_event_related_settings(sender, instance: AccEvent, **kwargs):
    instance.event_rules = EventRules.objects.create()
    instance.assist_rules = AssistRules.objects.create()
    instance.event_settings = EventSettings.objects.create()
    instance.server_config = ServerConfig.objects.create()
    instance.server_settings = ServerSettings.objects.create()


@receiver(signals.pre_save, sender=AccEvent)
def save_event_related_settings(sender, instance: AccEvent, **kwargs):
    instance.server_config.save()
    instance.server_settings.save()
    instance.assist_rules.save()
    instance.event_settings.save()
    instance.event_rules.save()
