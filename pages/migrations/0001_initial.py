# Generated by Django 3.1.8 on 2021-04-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('slug', models.SlugField()),
                ('featured_image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('rank', models.IntegerField(default=0)),
                ('is_in_navigation', models.BooleanField(default=True)),
                ('navigation_title', models.CharField(max_length=25)),
            ],
        ),
    ]
