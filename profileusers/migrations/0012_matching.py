# Generated by Django 3.2.4 on 2021-08-31 15:35

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0011_delete_matching'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_ititle', models.CharField(blank=True, default=None, max_length=254, null=True)),
                ('match_icity', models.CharField(max_length=50, null=True)),
                ('match_icountry', django_countries.fields.CountryField(max_length=2, null=True)),
                ('match_industry', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.industry')),
                ('match_iprofession', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.profession')),
                ('match_iskill', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.skill')),
            ],
        ),
    ]
