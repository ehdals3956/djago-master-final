# Generated by Django 3.1 on 2022-12-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20221220_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='CVV',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Expiration',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cardname',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cardnum',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='productnum',
            field=models.TextField(blank=True),
        ),
    ]
