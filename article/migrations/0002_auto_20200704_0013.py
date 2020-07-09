# Generated by Django 2.2.7 on 2020-07-03 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_auto_20200704_0013'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtypes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forums.SubTypes', verbose_name='Подвид'),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forums.Types', verbose_name='Вид'),
        ),
    ]