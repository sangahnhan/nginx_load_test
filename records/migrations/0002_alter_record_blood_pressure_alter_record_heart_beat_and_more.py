# Generated by Django 4.0.4 on 2022-05-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='blood_pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='heart_beat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='oxygen_saturation',
            field=models.IntegerField(),
        ),
    ]
