# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_profile', '0002_auto_20150919_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libprofile',
            name='books_issued',
        ),
    ]
