# Generated by Django 3.2.6 on 2022-10-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField(verbose_name='href')),
                ('content_name', models.CharField(max_length=200)),
                ('guid', models.CharField(max_length=100)),
            ],
        ),
    ]
