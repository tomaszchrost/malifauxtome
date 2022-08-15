# Generated by Django 4.0.6 on 2022-08-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0013_alter_action_triggers_alter_malifauxmodel_abilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='malifauxmodel',
            name='faction',
            field=models.CharField(choices=[('G', 'Guild'), ('R', 'Resurrectionists'), ('N', 'Neverborn'), ('A', 'Arcanists'), ('O', 'Outcasts'), ('B', 'Bayou'), ('T', 'Ten Thunders'), ('E', "Explorer's Society")], default='E', max_length=1),
            preserve_default=False,
        ),
    ]
