# Generated by Django 4.1 on 2022-09-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='type',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=200),
        ),
    ]
