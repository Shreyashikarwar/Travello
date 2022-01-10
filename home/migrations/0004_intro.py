# Generated by Django 3.2.7 on 2021-12-31 07:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211230_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introtitle', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('introdesc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('introimg', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
