# Generated by Django 3.2.3 on 2021-05-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0013_alter_stats_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='country_flag',
            field=models.CharField(default='/static/images/flags/DefaultFlag.bmp', max_length=65),
        ),
    ]