# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskzilla', '0004_auto_20151011_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='subscribers',
            field=models.ManyToManyField(related_name='tasks', to='taskzilla.UserProfile'),
        ),
    ]
