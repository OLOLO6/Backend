# Generated by Django 2.2.7 on 2020-07-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200704_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]