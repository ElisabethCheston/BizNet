# Generated by Django 3.2.4 on 2021-08-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0004_auto_20210813_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='picture',
            field=models.ImageField(default='profileavatar.png', upload_to='images'),
        ),
    ]
