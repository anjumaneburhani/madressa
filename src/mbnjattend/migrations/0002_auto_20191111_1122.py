# Generated by Django 2.2.5 on 2019-11-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbnjattend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='desc',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Status'),
        ),
    ]
