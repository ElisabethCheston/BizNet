# Generated by Django 3.2.4 on 2021-11-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20211124_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=models.TextField(default=''),
        ),
    ]