# Generated by Django 2.2.3 on 2019-07-25 14:46

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190725_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
