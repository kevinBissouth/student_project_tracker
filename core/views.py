from django.shortcuts import render

def home(request):
    """Page d'accueil publique de l'application."""
    return render(request, 'landing/home.html')

def privacy_policy(request):
    """Page Politique de confidentialité."""
    return render(request, 'pages/privacy.html')

def terms_of_service(request):
    """Page Conditions d'utilisation."""
    return render(request, 'pages/terms.html')

def user_guide(request):
    """Page Guide d'utilisation."""
    return render(request, 'pages/guide.html')

def documentation(request):
    """Page Documentation technique."""
    return render(request, 'pages/docs.html')
