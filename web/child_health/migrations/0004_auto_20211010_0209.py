# Generated by Django 3.2.7 on 2021-10-10 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child_health', '0003_auto_20211010_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='child',
            index=models.Index(fields=['user'], name='child_healt_user_id_dbedfb_idx'),
        ),
        migrations.AddIndex(
            model_name='child',
            index=models.Index(fields=['date_of_birth'], name='child_healt_date_of_d3f06f_idx'),
        ),
    ]
