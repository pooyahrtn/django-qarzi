# Generated by Django 2.2.3 on 2019-08-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20190821_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basefeed',
            name='lat',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='basefeed',
            name='long',
            field=models.DecimalField(db_index=True, decimal_places=4, max_digits=8),
        ),
    ]
