# Generated by Django 5.1.3 on 2024-11-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_person_login_id_alter_person_login_pw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="login_pw",
            field=models.CharField(max_length=19),
        ),
        migrations.AlterField(
            model_name="person",
            name="name",
            field=models.CharField(max_length=21),
        ),
    ]
