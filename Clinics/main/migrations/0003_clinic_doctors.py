# Generated by Django 5.0 on 2023-12-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctors", "0001_initial"),
        ("main", "0002_alter_clinic_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="clinic",
            name="doctors",
            field=models.ManyToManyField(to="doctors.doctor"),
        ),
    ]
