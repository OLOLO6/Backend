# Generated by Django 2.2.7 on 2020-06-21 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200621_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialty',
            old_name='title_kg',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='title_ru',
        ),
    ]