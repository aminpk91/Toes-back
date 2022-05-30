# Generated by Django 3.2.12 on 2022-03-30 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_login_register', '0004_auto_20220316_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=250, unique=True, verbose_name='کاربر'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='activate',
            field=models.BooleanField(default=False, verbose_name='فاعل بودن یا نبودن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=250, verbose_name='شماره موبایل'),
        ),
    ]