# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0006_auto_20150312_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.ImageField(upload_to=b'item_images', blank=True),
            preserve_default=True,
        ),
    ]
