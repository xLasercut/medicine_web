# Generated by Django 2.2.8 on 2019-12-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinepage',
            name='eng_name',
            field=models.TextField(default='', verbose_name='英文名'),
        ),
        migrations.AddField(
            model_name='medicinepage',
            name='latin_name',
            field=models.TextField(default='', verbose_name='拉丁名'),
        ),
    ]
