# Generated by Django 5.1.1 on 2024-09-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="payload",
            field=models.CharField(default="", max_length=180),
        ),
    ]
