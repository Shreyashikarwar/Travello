# Generated by Django 3.2.7 on 2021-12-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20211227_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='chooseus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
