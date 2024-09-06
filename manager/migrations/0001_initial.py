# Generated by Django 5.1 on 2024-09-06 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('route_end', models.CharField(max_length=50)),
                ('route_distance', models.IntegerField()),
                ('route_price', models.IntegerField()),
                ('route_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starting_routes', to='manager.city')),
                ('route_start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ending_routes', to='manager.city')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(max_length=50)),
                ('seating_capacity', models.IntegerField()),
                ('route_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.route')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50)),
                ('stage_location', models.CharField(max_length=50)),
                ('city_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='manager.city')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='stage_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.stage'),
        ),
    ]
