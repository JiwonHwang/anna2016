# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
