# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170419_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, auto_created=True),
        ),
    ]
