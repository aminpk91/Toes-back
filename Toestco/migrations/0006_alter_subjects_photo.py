# Generated by Django 3.2.12 on 2022-05-26 07:40

import Utils.Image_dir
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toestco', '0005_alter_subjects_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='Photo',
            field=models.ImageField(default=None, null=True, upload_to=Utils.Image_dir.Subject_image_directory_path, verbose_name='عکس'),
        ),
    ]