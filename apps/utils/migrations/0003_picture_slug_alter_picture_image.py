# Generated by Django 5.0.1 on 2024-07-02 19:20

import apps.utils.paths
import apps.utils.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_picture_utils_pictu_content_141a70_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp']), apps.utils.validators.ImageSizeValidator(max_height=3000, max_width=3000), apps.utils.validators.FileSizeValidator(limit_mb=1)], verbose_name='image'),
        ),
    ]
