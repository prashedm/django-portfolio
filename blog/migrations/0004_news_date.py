# Generated by Django 3.2.5 on 2021-07-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default='SOME STRING', verbose_name='Date'),
        ),
    ]