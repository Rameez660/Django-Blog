# Generated by Django 3.0.4 on 2020-03-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('contact', models.CharField(default='', max_length=70)),
                ('author', models.CharField(default='', max_length=70)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
