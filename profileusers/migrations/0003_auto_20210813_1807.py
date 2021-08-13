# Generated by Django 3.2.4 on 2021-08-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0002_auto_20210813_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Professions',
            },
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='profession',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.profession'),
        ),
    ]
