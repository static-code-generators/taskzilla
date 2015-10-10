# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskzilla', '0008_auto_20151011_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(default='')),
                ('task', models.ForeignKey(to='taskzilla.Task')),
            ],
        ),
    ]
