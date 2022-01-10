# Generated by Django 3.2.7 on 2021-12-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_bgimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=20, null=True)),
                ('msg', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='username',
        ),
    ]
