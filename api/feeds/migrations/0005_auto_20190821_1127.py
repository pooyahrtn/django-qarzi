# Generated by Django 2.2.3 on 2019-08-21 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20190727_0723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basefeed',
            options={'ordering': ['-created_time']},
        ),
    ]
