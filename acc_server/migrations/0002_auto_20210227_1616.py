# Generated by Django 3.1.7 on 2021-02-27 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc_server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistrules',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventrules',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventsettings',
            name='event',
        ),
        migrations.RemoveField(
            model_name='serverconfig',
            name='event',
        ),
        migrations.RemoveField(
            model_name='serversettings',
            name='event',
        ),
        migrations.RemoveField(
            model_name='session',
            name='event_settings',
        ),
        migrations.AddField(
            model_name='event',
            name='assist_rules',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='acc_server.assistrules'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_rules',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='acc_server.eventrules'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='acc_server.eventsettings'),
        ),
        migrations.AddField(
            model_name='event',
            name='server_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='acc_server.serverconfig'),
        ),
        migrations.AddField(
            model_name='event',
            name='server_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='acc_server.serversettings'),
        ),
        migrations.AlterField(
            model_name='eventrules',
            name='max_drivers_count',
            field=models.IntegerField(default=100),
        ),
    ]
