from django.db import models


class Utilisateurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=150)


class TypePlat(models.Model):
    type = models.CharField(max_length=50)


class Ingrédients(models.Model):
    nom = models.CharField(max_length=100)


class Recette(models.Model):
    titre = models.CharField(max_length=100)
    type = models.ForeignKey(TypePlat)
    cout = models.FloatField()
    temps_preparation = models.IntegerField(default=0)
    temps_cuisson = models.IntegerField(default=0)
    temps_repos = models.IntegerField(default=0)
    note_moyenne = models.FloatField(default=0)
    utilisateur_id = models.ForeignKey(Utilisateurs)
    creation_date = models.DateField()
    dernière_modification_date = models.DateField()


class Recette_Ingredients(models.Model):
    recette_id = models.ForeignKey(Recette)
    ingredient_id = models.ForeignKey(Ingrédients)
    quantite = models.FloatField()


class Commentaire(models.Model):
    utilisateur_id = models.ForeignKey(Utilisateurs)
    recette_id = models.ForeignKey(Recette)
    note = models.FloatField(null=True, blank=True)
    commentaire = models.CharField(max_length=500)
