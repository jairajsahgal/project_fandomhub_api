# Generated by Django 5.0.1 on 2024-05-28 20:16

import apps.utils.paths
import apps.utils.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utils.validators.ImageSizeValidator(max_height=1080, max_width=1080), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='image'),
        ),
    ]
