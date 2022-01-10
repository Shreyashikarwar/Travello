# Generated by Django 3.2.7 on 2021-12-31 06:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211231_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('discountsub', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='news',
            name='discountsub',
        ),
    ]