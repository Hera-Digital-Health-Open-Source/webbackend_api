# Generated by Django 4.0.1 on 2022-01-23 09:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_survey_responded_at_survey_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='available_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
