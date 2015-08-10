# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('website', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('edition', models.IntegerField()),
                ('authors', models.ManyToManyField(to='admin_interface.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=40)),
                ('website', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Research_paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(to='admin_interface.Author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='courses',
            field=models.ManyToManyField(to='admin_interface.Course'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='admin_interface.Publisher'),
        ),
    ]
