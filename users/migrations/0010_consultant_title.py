# Generated by Django 2.2.7 on 2020-07-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200622_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
    ]
