# Generated by Django 4.0.6 on 2022-08-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0009_malifauxmodel_cost_alter_action_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='resist',
            field=models.CharField(max_length=50),
        ),
    ]