# Generated by Django 4.1 on 2022-09-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_tabletennismodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='weightliftingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameoftournament', models.CharField(choices=[('WORLD_WEIGHTLIFTING_CHAMPIONSHIP', 'WORLD_WEIGHTLIFTING_CHAMPIONSHIP'), ('INTERNATIONAL_WEIGHTLIFTING_FEDERATION', 'INTERNATIONAL_WEIGHTLIFTING_FEDERATION'), ('IWLF_YOUNG_NATION_WEIGHTLIFTING_CHAMPIONSHIP', 'IWLF_YOUNG_NATION_WEIGHTLIFTING_CHAMPIONSHIP'), ('IWLF_JUNIOR_NATION_WEIGHTLIFTING_CHAMPIONSHIP', 'IWLF_JUNIOR_NATION_WEIGHTLIFTING_CHAMPIONSHIP'), ('COMMONWEALTH_GAMES', 'COMMONWEALTH_GAMES')], default='WORLD_WEIGHTLIFTING_CHAMPIONSHIP', max_length=200)),
                ('criteriaofage', models.CharField(choices=[('UNDER_19', 'UNDER_19'), ('UNDER_13', 'UNDER_13'), ('UNDER_21', 'UNDER_21')], default='UNDER_19', max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('dept', models.CharField(choices=[('LJMCA', 'LJMCA'), ('LJMBA', 'LJMBA')], default='LJMCA', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='tabletennismodel',
            name='nameoftournament',
            field=models.CharField(choices=[('TABLE_TENNIS_TOURS_AND_SERIES', 'TABLE_TENNIS_TOURS_AND_SERIES'), ('ASIAN_JUNIOR AND_CADET_TABLE_TENNIS_CHAMPIONSHIPS', 'ASIAN_JUNIOR AND_CADET_TABLE_TENNIS_CHAMPIONSHIPS'), ('HUNGRIAN_OPEN', 'HUNGRIAN_OPEN'), ('ITTP', 'ITTP'), ('PAN_AMERICAN_TABLE_TENNIS_CUP', 'PAN_AMERICAN_TABLE_TENNIS_CUP')], default='HUNGRIAN_OPEN', max_length=200),
        ),
    ]
