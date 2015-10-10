# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskzilla', '0007_auto_20151011_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
