# Generated by Django 5.1.3 on 2024-12-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsel', '0005_remove_counsel_counsel_date_counsel_counsel_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsel',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
