# Generated by Django 4.1 on 2022-09-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0003_evaluationusermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='tournamentuserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('sportsname', models.CharField(max_length=200)),
                ('dob', models.IntegerField()),
                ('dept', models.CharField(max_length=200)),
                ('achivement', models.CharField(max_length=200)),
            ],
        ),
    ]