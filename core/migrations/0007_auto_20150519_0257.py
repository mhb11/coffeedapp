# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150518_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='coffee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Pathetic'), (1, b'Passable'), (2, b'Good'), (3, b'Very Good'), (4, b'Best Ever')]),
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor_seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Scarce'), (2, b'Ample'), (3, b'Ton')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Scarce'), (2, b'Ample'), (3, b'Ton')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No WiFi'), (1, b'Weak'), (2, b'Strong')]),
        ),
    ]
