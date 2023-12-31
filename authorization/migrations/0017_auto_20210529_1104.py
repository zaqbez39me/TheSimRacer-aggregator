# Generated by Django 3.2.3 on 2021-05-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0016_stats_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='description',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='stats',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
