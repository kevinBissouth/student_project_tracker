from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Role(models.TextChoices):
    STUDENT = 'STUDENT', 'Étudiant'
    SUPERVISOR = 'SUPERVISOR', 'Encadreur'
    ADMIN = 'ADMIN', 'Administrateur'


class Filiere(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Code',
    )
    nom = models.CharField(
        max_length=100,
        verbose_name='Nom',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )

    class Meta:
        verbose_name = 'Filière'
        verbose_name_plural = 'Filières'
        ordering = ['code']

    def __str__(self):
        return self.code


class Niveau(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Code',
    )
    nom = models.CharField(
        max_length=50,
        verbose_name='Nom',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )

    class Meta:
        verbose_name = "Niveau d'étude"
        verbose_name_plural = "Niveaux d'étude"
        ordering = ['code']

    def __str__(self):
        return f'{self.code} — {self.nom}'


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name='Rôle',
    )
    # Champs liés à l'étudiant uniquement
    filiere = models.ForeignKey(
        Filiere,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Filière',
    )
    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Niveau d'étude",
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Téléphone',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Biographie',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',
    )

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

    def __str__(self):
        return f'{self.user.get_full_name() or self.user.username} ({self.get_role_display()})'

    def clean(self):
        """
        Règle métier :
        - Un étudiant doit avoir une filière ET un niveau.
        - Un encadreur ou un administrateur ne doit avoir NI filière NI niveau.
        """
        if self.role == Role.STUDENT:
            if not self.filiere:
                raise ValidationError({'filiere': 'Un étudiant doit avoir une filière.'})
            if not self.niveau:
                raise ValidationError({'niveau': "Un étudiant doit avoir un niveau d'étude."})
        else:
            if self.filiere:
                raise ValidationError({'filiere': 'Seul un étudiant peut avoir une filière.'})
            if self.niveau:
                raise ValidationError({'niveau': "Seul un étudiant peut avoir un niveau d'étude."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
