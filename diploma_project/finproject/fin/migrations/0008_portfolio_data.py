# Generated by Django 3.2 on 2022-06-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0007_remove_portfolio_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='data',
            field=models.TextField(blank=True),
        ),
    ]
