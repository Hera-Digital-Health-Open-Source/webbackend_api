# Generated by Django 3.2.9 on 2021-12-21 06:40

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20211220_1002'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='notificationevent',
            name='context',
            field=django.contrib.postgres.fields.hstore.HStoreField(default=dict),
        ),
    ]
