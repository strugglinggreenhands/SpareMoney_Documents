# Generated by Django 2.2.2 on 2019-06-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(default='0'),
        ),
    ]
