# Generated by Django 2.2.7 on 2020-06-16 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200615_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.Consultant', verbose_name='Консультант')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
