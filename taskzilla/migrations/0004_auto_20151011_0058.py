# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskzilla', '0003_auto_20151011_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tasks',
            field=models.ManyToManyField(related_name='subscribers', to='taskzilla.Task'),
        ),
    ]
