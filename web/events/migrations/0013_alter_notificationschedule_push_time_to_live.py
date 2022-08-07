# Generated by Django 4.0.1 on 2022-01-16 10:05

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_alter_notificationevent_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationschedule',
            name='push_time_to_live',
            field=models.DurationField(default=datetime.timedelta(days=1), help_text='(days hh:mm:ss) If this amount of time has passed after the calendar event, no notification will be generated.', validators=[django.core.validators.MinValueValidator(datetime.timedelta(seconds=300))], verbose_name='Duration until notification expires'),
        ),
    ]