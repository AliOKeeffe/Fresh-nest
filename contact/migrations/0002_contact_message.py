# Generated by Django 3.2 on 2022-09-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=500),
        ),
    ]
