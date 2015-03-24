from django.shortcuts import render


def Index(request):
    return render(request, 'site_recettes/index.html', {})