# Generated by Django 2.2.7 on 2020-08-11 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200808_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='rooms.Thread', verbose_name='Комната'),
        ),
    ]
