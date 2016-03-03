# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160223_2352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
