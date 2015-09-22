# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='courses',
            field=models.ManyToManyField(to='admin_interface.Course', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
