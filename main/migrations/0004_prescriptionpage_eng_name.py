# Generated by Django 2.2.8 on 2019-12-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionpage',
            name='eng_name',
            field=models.TextField(default='', verbose_name='英文名'),
        ),
    ]
