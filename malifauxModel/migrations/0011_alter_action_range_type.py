# Generated by Django 4.0.6 on 2022-08-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0010_alter_action_resist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='range_type',
            field=models.CharField(max_length=50),
        ),
    ]
