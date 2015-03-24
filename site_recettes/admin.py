from django.contrib import admin
from django.shortcuts import HttpResponse

# Register your models here.


def UtilisateurAdmin():
    return HttpResponse("Bienvenue!")