# Generated by Django 2.2.7 on 2020-08-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='updated',
        ),
        migrations.AddField(
            model_name='thread',
            name='access',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thread',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
