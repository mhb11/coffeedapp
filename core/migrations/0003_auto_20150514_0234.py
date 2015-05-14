# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150514_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(null=True, blank=True),
        ),
    ]
