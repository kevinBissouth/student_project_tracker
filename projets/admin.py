from django import forms
from django.contrib import admin

from accounts.models import Profile, Role
from .models import Category, Project, Task, ProjectComment, TaskComment


class ProjectAdminForm(forms.ModelForm):
    """
    Filtre les profils dans les champs student et supervisor
    pour n'afficher que les rôles correspondants.
    """

    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Profile.objects.filter(
            role=Role.STUDENT,
        )
        self.fields['supervisor'].queryset = Profile.objects.filter(
            role=Role.SUPERVISOR,
        )


class ProjectCommentAdminForm(forms.ModelForm):
    """
    L'auteur d'un commentaire de projet peut être un étudiant,
    un encadreur ou un administrateur.
    L'étudiant commente son propre projet pour échanger avec son encadreur.
    """

    class Meta:
        model = ProjectComment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Profile.objects.filter(
            role__in=[Role.STUDENT, Role.SUPERVISOR, Role.ADMIN],
        )


class TaskCommentAdminForm(forms.ModelForm):
    """
    Même règle que ProjectComment : un étudiant peut commenter
    ses propres tâches pour dialoguer avec son encadreur.
    """

    class Meta:
        model = TaskComment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Profile.objects.filter(
            role__in=[Role.STUDENT, Role.SUPERVISOR, Role.ADMIN],
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at',)
    list_per_page = 25


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    list_display = (
        'title',
        'student',
        'supervisor',
        'category',
        'status',
        'deadline',
        'created_at',
    )
    list_filter = ('status', 'category')
    search_fields = (
        'title',
        'student__user__username',
        'student__user__email',
        'student__user__first_name',
        'student__user__last_name',
        'supervisor__user__username',
        'supervisor__user__email',
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('student__user', 'supervisor__user', 'category')
    list_per_page = 25
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'category'),
        }),
        ('Acteurs', {
            'fields': ('student', 'supervisor'),
        }),
        ('Avancement', {
            'fields': ('status', 'deadline'),
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date', 'created_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'project__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('project',)
    list_per_page = 25
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Informations', {
            'fields': ('title', 'description', 'project'),
        }),
        ('Avancement', {
            'fields': ('status', 'due_date'),
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    form = ProjectCommentAdminForm

    list_display = ('project', 'author', 'created_at')
    search_fields = ('content', 'project__title', 'author__user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('project', 'author__user')
    list_per_page = 25


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    form = TaskCommentAdminForm

    list_display = ('task', 'author', 'created_at')
    search_fields = ('content', 'task__title', 'author__user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('task', 'author__user')
    list_per_page = 25
