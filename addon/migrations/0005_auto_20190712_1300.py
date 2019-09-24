# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-12 13:00
from __future__ import unicode_literals

import addon.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("addon", "0004_auto_20190606_0043")]

    operations = [
        migrations.AlterField(
            model_name="addon",
            name="identifier",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="addonversion",
            name="yaml",
            field=addon.fields.NonStrippingTextField(),
        ),
    ]