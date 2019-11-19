# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-19 04:24
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("addon", "0005_auto_20190712_1300")]

    operations = [
        migrations.RenameModel(old_name="Platform", new_name="Stack"),
        migrations.RemoveField(model_name="addonversion", name="platforms"),
        migrations.AddField(
            model_name="addonversion",
            name="config",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict
            ),
        ),
        migrations.AddField(
            model_name="addonversion",
            name="stacks",
            field=models.ManyToManyField(
                help_text="Stacks this tag of the addon supports",
                to="addon.Stack",
            ),
        ),
    ]