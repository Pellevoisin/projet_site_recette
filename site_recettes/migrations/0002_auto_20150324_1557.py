# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_recettes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('note', models.FloatField(null=True, blank=True)),
                ('commentaire', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingrédients',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('cout', models.FloatField()),
                ('temps_preparation', models.IntegerField(default=0)),
                ('temps_cuisson', models.IntegerField(default=0)),
                ('temps_repos', models.IntegerField(default=0)),
                ('note_moyenne', models.FloatField(default=0)),
                ('creation_date', models.DateField()),
                ('dernière_modification_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recette_Ingredients',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quantite', models.FloatField()),
                ('ingredient_id', models.ForeignKey(to='site_recettes.Ingrédients')),
                ('recette_id', models.ForeignKey(to='site_recettes.Recette')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypePlat',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recette',
            name='type',
            field=models.ForeignKey(to='site_recettes.TypePlat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recette',
            name='utilisateur_id',
            field=models.ForeignKey(to='site_recettes.Utilisateurs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='recette_id',
            field=models.ForeignKey(to='site_recettes.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='utilisateur_id',
            field=models.ForeignKey(to='site_recettes.Utilisateurs'),
            preserve_default=True,
        ),
    ]
