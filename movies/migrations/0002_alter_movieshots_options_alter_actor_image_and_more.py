# Generated by Django 4.0.5 on 2022-10-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieshots',
            options={'verbose_name': 'Кадр из фильма', 'verbose_name_plural': 'Кадры из фильма'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(upload_to='media/actors/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='media/poster/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='image',
            field=models.ImageField(upload_to='media/movie_shots/', verbose_name='Изображение'),
        ),
        migrations.AlterModelTable(
            name='movieshots',
            table=None,
        ),
    ]
