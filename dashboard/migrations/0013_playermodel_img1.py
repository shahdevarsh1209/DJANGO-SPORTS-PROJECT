# Generated by Django 4.1 on 2022-10-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_volleyballmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermodel',
            name='img1',
            field=models.ImageField(default='', upload_to='player'),
        ),
    ]
