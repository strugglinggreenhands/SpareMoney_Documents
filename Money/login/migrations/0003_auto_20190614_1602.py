# Generated by Django 2.2.2 on 2019-06-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.IntegerField(default='0', max_length=32),
        ),
    ]
