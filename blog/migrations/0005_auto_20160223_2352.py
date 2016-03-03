# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
