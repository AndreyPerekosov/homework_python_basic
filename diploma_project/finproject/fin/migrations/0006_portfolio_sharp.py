# Generated by Django 3.2 on 2022-06-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0005_auto_20220620_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='sharp',
            field=models.FloatField(null=True),
        ),
    ]
