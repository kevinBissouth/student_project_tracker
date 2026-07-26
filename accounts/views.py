from django.shortcuts import render

def register(request):
    """Page d'inscription — à implémenter avec un formulaire d'enregistrement."""
    return render(request, 'auth-register.html')
