# Generated by Django 2.2.3 on 2019-08-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notification_token',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
