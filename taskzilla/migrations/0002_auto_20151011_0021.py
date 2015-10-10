# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskzilla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='subscribers',
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
