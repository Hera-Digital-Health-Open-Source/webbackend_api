# Generated by Django 3.2.7 on 2021-11-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_health', '0009_vaccine_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=20),
        ),
    ]
