# Generated by Django 4.0.3 on 2022-03-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_alter_survey_index_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveytemplatetranslation',
            name='language_code',
            field=models.CharField(choices=[('en', 'English'), ('tr', 'Turkish'), ('ar', 'Arabic'), ('ps', 'Pashto'), ('prs', 'Dari')], max_length=5),
        ),
    ]
