# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
    ]
