# Generated by Django 4.0.6 on 2022-07-18 20:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('malifauxModel', '0005_alter_keyword_name_alter_malifauxmodel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordAdmin',
            fields=[
                ('keyword_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='malifauxModel.keyword')),
            ],
            bases=('malifauxModel.keyword',),
        ),
        migrations.CreateModel(
            name='MalifauxModelAdmin',
            fields=[
                ('malifauxmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='malifauxModel.malifauxmodel')),
            ],
            bases=('malifauxModel.malifauxmodel',),
        ),
        migrations.CreateModel(
            name='StatCardAdmin',
            fields=[
                ('statcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='malifauxModel.statcard')),
            ],
            bases=('malifauxModel.statcard',),
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('suit', models.CharField(max_length=6)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.RenameField(
            model_name='malifauxmodel',
            old_name='keyword',
            new_name='keywords',
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='base_size',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='defence',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='movement',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='size',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='willpower',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statcard',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('action_type', models.CharField(choices=[('AA', 'Attack Action'), ('TA', 'Tactical Action')], max_length=2)),
                ('range_type', models.CharField(choices=[('ME', 'Melee'), ('PR', 'Projectile'), ('PU', 'Pulse'), ('AU', 'Aura'), ('NO', 'None')], max_length=2)),
                ('range', models.CharField(max_length=2)),
                ('stat', models.CharField(max_length=2)),
                ('resist', models.CharField(choices=[('Df', 'Df'), ('Wp', 'Wp'), ('Mv', 'Mv'), ('Sz', 'Sz')], max_length=2)),
                ('target_number', models.CharField(max_length=2)),
                ('description', ckeditor.fields.RichTextField()),
                ('bonus_action', models.BooleanField()),
                ('triggers', models.ManyToManyField(to='malifauxModel.trigger')),
            ],
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='abilities',
            field=models.ManyToManyField(to='malifauxModel.ability'),
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='actions',
            field=models.ManyToManyField(to='malifauxModel.action'),
        ),
        migrations.AddField(
            model_name='malifauxmodel',
            name='characteristics',
            field=models.ManyToManyField(to='malifauxModel.characteristic'),
        ),
    ]