# Generated by Django 4.1 on 2022-09-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_footballmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='basketballModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameoftournament', models.CharField(choices=[('ASIAN_CHAMPIONSHIPS', 'ASIAN_CHAMPIONSHIPS'), ('AFRICAN_CHAMPIONSHIPS', 'AFRICAN_CHAMPIONSHIPS'), ('EUROPEAN_CHAMPIONSHIPS', 'EUROPEAN_CHAMPIONSHIPS')], default='ASIAN_CHAMPIONSHIPS', max_length=200)),
                ('criteriaofage', models.CharField(choices=[('UNDER_19', 'UNDER_19'), ('UNDER_13', 'UNDER_13'), ('UNDER_21', 'UNDER_21')], default='UNDER_19', max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('dept', models.CharField(choices=[('LJMCA', 'LJMCA'), ('LJMBA', 'LJMBA')], default='LJMCA', max_length=50)),
            ],
        ),
    ]
