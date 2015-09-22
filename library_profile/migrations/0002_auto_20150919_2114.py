# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libprofile',
            name='books_issued',
            field=models.ForeignKey(blank=True, to='admin_interface.Book', null=True),
        ),
    ]
