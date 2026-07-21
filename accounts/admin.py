from django import forms
from django.contrib import admin

from .models import Filiere, Niveau, Profile, Role


class ProfileAdminForm(forms.ModelForm):
    """
    Rend les champs filière et niveau invisibles pour les non-étudiants.
    La validation métier est assurée par Profile.clean().
    """

    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            return

        # Cacher filiere et niveau quand le rôle n'est pas STUDENT
        if self.instance.role != Role.STUDENT:
            self.fields['filiere'].widget = forms.HiddenInput()
            self.fields['niveau'].widget = forms.HiddenInput()
            self.fields['filiere'].required = False
            self.fields['niveau'].required = False


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'created_at')
    search_fields = ('code', 'nom')
    ordering = ('code',)
    readonly_fields = ('created_at',)


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'created_at')
    search_fields = ('code', 'nom')
    ordering = ('code',)
    readonly_fields = ('created_at',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm

    list_display = ('user', 'role', 'filiere', 'niveau', 'phone', 'created_at')
    list_filter = ('role', 'filiere', 'niveau')
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    )
    ordering = ('user__last_name', 'user__first_name')
    readonly_fields = ('created_at',)
    list_per_page = 25
    list_select_related = ('filiere', 'niveau')

    def get_fieldsets(self, request, obj=None):
        """
        Adapte les sections affichées selon le rôle :
        - SUPERVISOR / ADMIN → section étudiant masquée.
        - STUDENT → filiere et niveau visibles.
        """
        if obj and obj.role != Role.STUDENT:
            return (
                ('Informations générales', {
                    'fields': ('user', 'role', 'phone', 'bio'),
                }),
                ('Dates', {
                    'fields': ('created_at',),
                }),
            )
        return (
            ('Informations générales', {
                'fields': ('user', 'role'),
            }),
            ('Informations étudiant', {
                'fields': ('filiere', 'niveau'),
            }),
            ('Contact', {
                'fields': ('phone', 'bio'),
            }),
            ('Dates', {
                'fields': ('created_at',),
            }),
        )
