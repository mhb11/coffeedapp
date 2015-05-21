# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150519_0257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='outdoor_seating',
            new_name='outdoor',
        ),
    ]
