# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 5, 9, 35, 938875, tzinfo=utc), editable=False, auto_created=True),
        ),
    ]
