# Generated by Django 2.2.3 on 2019-07-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basefeed',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
