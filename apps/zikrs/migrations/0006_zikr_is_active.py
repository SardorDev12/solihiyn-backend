# Generated by Django 5.0.1 on 2024-02-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zikrs', '0005_zikr_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='zikr',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
