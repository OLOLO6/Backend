# Generated by Django 2.2.7 on 2020-07-30 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200723_0118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryConsultant',
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
    ]
