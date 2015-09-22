# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_profile', '0003_remove_libprofile_books_issued'),
        ('admin_interface', '0002_auto_20150919_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='issuer',
            field=models.ForeignKey(default=None, blank=True, to='library_profile.libprofile', null=True),
        ),
    ]
