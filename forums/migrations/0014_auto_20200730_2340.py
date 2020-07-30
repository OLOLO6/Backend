# Generated by Django 2.2.7 on 2020-07-30 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200730_2340'),
        ('forums', '0013_auto_20200722_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subtypes',
            name='type',
        ),
        migrations.RemoveField(
            model_name='types',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='forum',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.SubCategory', verbose_name='Подкатегории'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='subtypes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.SubTypes', verbose_name='Подвиды'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Types', verbose_name='Виды'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='SubTypes',
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
