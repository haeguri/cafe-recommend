# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170419_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='create_date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
