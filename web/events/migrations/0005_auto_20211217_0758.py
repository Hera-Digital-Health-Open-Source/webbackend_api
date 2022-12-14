# Generated by Django 3.2.9 on 2021-12-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20211216_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationevent',
            name='event_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='notificationevent',
            unique_together={('event_key', 'schedule')},
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='object_id',
        ),
    ]
