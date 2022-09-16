# Generated by Django 4.1 on 2022-09-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='cricketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameoftournament', models.CharField(choices=[('REDBULL_CUP', 'REDBULL_CUP'), ('DULEEP_TROPHY', 'DULEEP_TROPHY'), ('RANJI_TROPHY', 'RANJI_TROPHY'), ('VIJAY_HAZARE', 'VIJAY_HAZARE'), ('IPL', 'IPL')], default='REDBULL_CUP', max_length=200)),
                ('criteriaofage', models.CharField(choices=[('UNDER_19', 'UNDER_19'), ('UNDER_13', 'UNDER_13'), ('UNDER_21', 'UNDER_21')], default='UNDER_19', max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('dept', models.CharField(choices=[('LJMCA', 'LJMCA'), ('LJMBA', 'LJMBA')], default='LJMCA', max_length=50)),
                ('ground', models.CharField(choices=[('NAREDRA_MODI_GROUND', 'NAREDRA_MODI_GROUND'), ('C_B_PATEL_INTERNATION_CRICKET_GROUND', 'C_B_PATEL_INTERNATION_CRICKET_GROUND'), ('GUJARAT_COLLEGE_GROUND', 'GUJARAT_COLLEGE_GROUND')], default='NAREDRA_MODI_GROUND', max_length=50)),
            ],
        ),
    ]
