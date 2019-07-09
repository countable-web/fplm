# Generated by Django 2.2.3 on 2019-07-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0009_auto_20190705_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagemember',
            name='language',
        ),
        migrations.RemoveField(
            model_name='placename',
            name='language',
        ),
        migrations.AddField(
            model_name='placename',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='champion',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='dialect',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='languagefamily',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='languagesubfamily',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]