# Generated by Django 2.2.3 on 2019-09-13 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggests', '0003_auto_20190821_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basesuggest',
            options={'ordering': ['-created_time']},
        ),
    ]