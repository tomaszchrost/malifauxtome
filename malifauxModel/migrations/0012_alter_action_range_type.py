# Generated by Django 4.0.6 on 2022-08-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0011_alter_action_range_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='range_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]