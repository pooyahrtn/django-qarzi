# Generated by Django 2.2.3 on 2019-07-25 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20190725_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowfeed',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='lendfeed',
            old_name='uuid',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='borrowfeed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='uuid'),
        ),
        migrations.AlterField(
            model_name='lendfeed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='uuid'),
        ),
    ]
