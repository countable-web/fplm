# Generated by Django 2.2.4 on 2019-09-22 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_administrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_notified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]