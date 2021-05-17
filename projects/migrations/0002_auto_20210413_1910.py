# Generated by Django 3.2 on 2021-04-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
