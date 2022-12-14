# Generated by Django 4.0.1 on 2022-01-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_notificationschedule_push_time_to_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationschedule',
            name='notification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.notificationtype'),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='notification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.notificationtype'),
        ),
    ]
