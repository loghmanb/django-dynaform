# Generated by Django 4.2.5 on 2023-09-27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DynaForm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Name"),
                ),
                ("label", models.CharField(max_length=50, verbose_name="Label")),
                ("structure", models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name="DynaFormData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.JSONField(default=dict)),
                ("list_order", models.IntegerField()),
                (
                    "dynaform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dynaform.dynaform",
                    ),
                ),
            ],
        ),
    ]
