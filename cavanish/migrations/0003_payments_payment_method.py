# Generated by Django 5.0.1 on 2024-01-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cavanish', '0002_payments_payment_made_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(choices=[('Online', 'Through our Application'), ('Cash', 'Cash Deposit')], max_length=99, null=True),
        ),
    ]
