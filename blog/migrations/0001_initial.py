# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(default='')),
                ('post_num', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.TextField(default='')),
                ('visit_count', models.IntegerField(default=0)),
                ('pub_date', models.DateField(auto_now_add=True, auto_now=True)),
                ('abstract', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('classification', models.ForeignKey(to='blog.Classification')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
