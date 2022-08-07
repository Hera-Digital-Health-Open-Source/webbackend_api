# Generated by Django 3.2.9 on 2021-12-16 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('events', '0003_auto_20211211_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationevent',
            name='notification_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.notificationtype'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='NotificationSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_event_type', models.CharField(choices=[('prenatal_checkup', 'Prenatal Checkup'), ('vaccination', 'Vaccination')], max_length=50)),
                ('offset_days', models.SmallIntegerField()),
                ('time_of_day', models.TimeField()),
                ('push_time_to_live', models.DurationField(default=datetime.timedelta(days=1))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.notificationtype')),
            ],
            options={
                'unique_together': {('calendar_event_type', 'offset_days', 'time_of_day')},
            },
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.notificationschedule'),
        ),
        migrations.AlterUniqueTogether(
            name='notificationevent',
            unique_together={('content_type', 'object_id', 'schedule')},
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='body',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='title',
        ),
    ]
