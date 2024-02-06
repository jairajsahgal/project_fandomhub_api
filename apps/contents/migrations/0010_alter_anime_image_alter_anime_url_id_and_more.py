# Generated by Django 5.0.1 on 2024-02-06 18:20

import apps.utils.paths
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0009_alter_anime_duration_alter_anime_genre_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='url_id',
            field=models.ManyToManyField(blank=True, to='contents.url'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.author'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='demographic_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.demographic'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='genre_id',
            field=models.ManyToManyField(blank=True, to='contents.genre'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='release',
            field=models.DateField(blank=True, null=True, verbose_name='Release'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='synopsis',
            field=models.TextField(blank=True, null=True, verbose_name='Synopsis'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='url_id',
            field=models.ManyToManyField(blank=True, to='contents.url'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, verbose_name='Image'),
        ),
    ]
