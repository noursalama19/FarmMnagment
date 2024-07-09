# Generated by Django 4.2.13 on 2024-07-08 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("size", models.FloatField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Crop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("planting_date", models.DateField()),
                ("harvest_date", models.DateField()),
                (
                    "farm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="FarmMangment.farm",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("species", models.CharField(max_length=255)),
                ("birth_date", models.DateField()),
                (
                    "farm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="FarmMangment.farm",
                    ),
                ),
            ],
        ),
    ]