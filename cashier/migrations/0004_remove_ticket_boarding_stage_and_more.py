# Generated by Django 5.1 on 2024-09-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0003_ticket_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='boarding_stage',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa')], default='Cash', max_length=100),
        ),
    ]
