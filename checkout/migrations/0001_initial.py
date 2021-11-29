# Generated by Django 3.2.4 on 2021-11-29 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=254, null=True)),
                ('stripe_customer_id', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_bag', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('membership', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.membership')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription', to='membership.usermembership')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.subscription')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.membership')),
            ],
        ),
    ]
