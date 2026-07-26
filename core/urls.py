from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confidentialite/', views.privacy_policy, name='privacy'),
    path('conditions/', views.terms_of_service, name='terms'),
    path('guide/', views.user_guide, name='guide'),
    path('documentation/', views.documentation, name='docs'),
]
