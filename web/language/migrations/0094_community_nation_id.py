# Generated by Django 2.2.4 on 2019-11-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0093_merge_20191104_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='nation_id',
            field=models.IntegerField(null=True),
        ),
    ]