# Generated by Django 3.2.7 on 2021-12-30 09:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('client', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]