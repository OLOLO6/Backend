# Generated by Django 2.2.7 on 2020-07-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_delete_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_image',
            field=models.ImageField(blank=True, null=True, upload_to='category-icon/', verbose_name='Иконка'),
        ),
    ]