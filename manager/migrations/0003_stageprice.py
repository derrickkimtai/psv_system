# Generated by Django 5.1 on 2024-09-09 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_route_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='StagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='manager.route')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='manager.stage')),
            ],
            options={
                'unique_together': {('route', 'stage')},
            },
        ),
    ]
