# Generated by Django 5.0.1 on 2024-04-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_alter_anime_num_list_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='num_scoring_users',
        ),
        migrations.AddField(
            model_name='anime',
            name='favorites',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='favorites'),
        ),
    ]
