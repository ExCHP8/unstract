# Generated by Django 4.2.1 on 2024-08-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prompt_studio", "0006_alter_toolstudioprompt_prompt_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toolstudioprompt",
            name="enforce_type",
            field=models.TextField(
                blank=True,
                choices=[
                    ("Text", "Response sent as Text"),
                    ("number", "Response sent as number"),
                    ("email", "Response sent as email"),
                    ("date", "Response sent as date"),
                    ("boolean", "Response sent as boolean"),
                    ("json", "Response sent as json"),
                    ("table", "Response sent as table"),
                ],
                db_comment="Field to store the type in             which the response to be returned.",
                default="Text",
            ),
        ),
    ]