# Generated by Django 5.0.3 on 2024-05-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='massage',
            field=models.CharField(default='', max_length=50),
        ),
    ]
