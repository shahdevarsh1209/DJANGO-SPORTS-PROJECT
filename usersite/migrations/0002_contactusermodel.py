# Generated by Django 4.1 on 2022-09-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactuserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('Number', models.IntegerField()),
                ('WriteSomething', models.CharField(max_length=200)),
            ],
        ),
    ]
