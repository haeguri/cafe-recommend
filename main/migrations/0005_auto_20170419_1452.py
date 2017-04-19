# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170419_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]
