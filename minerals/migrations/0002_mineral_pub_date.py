# Generated by Django 2.0.3 on 2018-03-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='pub_date',
            field=models.DateTimeField(default='1990-01-25 00:00:00'),
        ),
    ]
