# Generated by Django 3.2.5 on 2021-07-10 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]
