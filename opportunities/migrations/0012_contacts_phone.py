# Generated by Django 3.2.4 on 2021-11-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_auto_20211117_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
