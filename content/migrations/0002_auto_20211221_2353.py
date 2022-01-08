# Generated by Django 3.2.9 on 2021-12-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_file',
        ),
        migrations.AddField(
            model_name='movie',
            name='moviefile',
            field=models.FileField(blank=True, upload_to='', verbose_name='Upload the movie: '),
        ),
        migrations.AddField(
            model_name='movie',
            name='movielink',
            field=models.FileField(blank=True, upload_to='', verbose_name='Upload the movie: '),
        ),
    ]