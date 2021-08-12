# Generated by Django 3.2.4 on 2021-08-11 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, upload_to='images')),
                ('city', models.CharField(default='City', max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('gigdescription', models.TextField(max_length=250, null=True)),
                ('extrainfo', models.TextField(max_length=250, null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profileusers.profileuser')),
                ('industry', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.industry')),
                ('liked', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
