# Generated by Django 3.2 on 2022-10-13 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_testimonial_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previousproject',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image_url',
        ),
    ]