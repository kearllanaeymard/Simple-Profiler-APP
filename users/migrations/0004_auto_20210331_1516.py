# Generated by Django 3.1.7 on 2021-03-31 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210327_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 31, 7, 16, 2, 934383, tzinfo=utc)),
        ),
    ]
