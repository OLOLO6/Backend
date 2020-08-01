# Generated by Django 2.2.7 on 2020-07-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200722_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='comment_kg',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='comment_ru',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='description_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='title_kg',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='title_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='text_kg',
            field=models.TextField(max_length=5000, null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='text_ru',
            field=models.TextField(max_length=5000, null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='title_kg',
            field=models.CharField(max_length=100, null=True, verbose_name='Специальность'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Специальность'),
        ),
    ]