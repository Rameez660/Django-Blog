# Generated by Django 3.0.4 on 2020-03-21 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contact',
            new_name='content',
        ),
    ]
