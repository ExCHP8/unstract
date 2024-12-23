# Generated by Django 4.2.1 on 2024-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prompt_studio_v2", "0003_toolstudioprompt_required"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toolstudioprompt",
            name="required",
            field=models.CharField(
                blank=True,
                choices=[("all", "All values required"), ("any", "Any value required")],
                default=None,
                max_length=3,
                null=True,
            ),
        ),
    ]