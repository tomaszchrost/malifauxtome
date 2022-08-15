# Generated by Django 4.0.6 on 2022-08-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0012_alter_action_range_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='triggers',
            field=models.ManyToManyField(blank=True, to='malifauxModel.trigger'),
        ),
        migrations.AlterField(
            model_name='malifauxmodel',
            name='abilities',
            field=models.ManyToManyField(blank=True, to='malifauxModel.ability'),
        ),
    ]
