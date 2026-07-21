
from django.db import models

from accounts.models import Profile


class StatutProjet(models.TextChoices):
    DRAFT = 'DRAFT', 'Brouillon'
    WAITING_SUPERVISOR = 'WAITING_SUPERVISOR', 'En attente d\'un encadreur'
    IN_PROGRESS = 'IN_PROGRESS', 'En cours'
    COMPLETED = 'COMPLETED', 'Terminé'
    CANCELLED = 'CANCELLED', 'Annulé'


class StatutTache(models.TextChoices):
    TODO = 'TODO', 'À faire'
    IN_PROGRESS = 'IN_PROGRESS', 'En cours'
    DONE = 'DONE', 'Terminé'
    BLOCKED = 'BLOCKED', 'Bloqué'


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nom',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Titre',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )
    student = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='projects_as_student',
        verbose_name='Étudiant',
    )
    supervisor = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects_as_supervisor',
        verbose_name='Encadreur',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='projects',
        verbose_name='Catégorie',
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date limite',
    )
    status = models.CharField(
        max_length=20,
        choices=StatutProjet.choices,
        default=StatutProjet.DRAFT,
        verbose_name='Statut',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Projet',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Titre',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )
    status = models.CharField(
        max_length=20,
        choices=StatutTache.choices,
        default=StatutTache.TODO,
        verbose_name='Statut',
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date d'échéance",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    class Meta:
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'

    def __str__(self):
        return self.title


class ProjectComment(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_comments',
        verbose_name='Projet',
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='project_comments',
        verbose_name='Auteur',
    )
    content = models.TextField(
        verbose_name='Contenu',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    class Meta:
        verbose_name = 'Commentaire de projet'
        verbose_name_plural = 'Commentaires de projets'

    def __str__(self):
        return f'Commentaire de {self.author} sur {self.project}'


class TaskComment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='task_comments',
        verbose_name='Tâche',
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='task_comments',
        verbose_name='Auteur',
    )
    content = models.TextField(
        verbose_name='Contenu',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    class Meta:
        verbose_name = 'Commentaire de tâche'
        verbose_name_plural = 'Commentaires de tâches'

    def __str__(self):
        return f'Commentaire de {self.author} sur {self.task}'
