from django.db import models

class ResponsableLegal(models.Model):
    nom = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Adherent(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    responsable_legal = models.ForeignKey(ResponsableLegal, on_delete=models.SET_NULL, null=True, blank=True)
    statut_cotisation = models.CharField(max_length=50, choices=[('Payée', 'Payée'), ('En attente', 'En attente'), ('Non payée', 'Non payée')], default='En attente')
    badge_id = models.CharField(max_length=50, unique=True)
    cours_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nom

from django.utils import timezone

class Presence(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.adherent.nom} - {self.date} - {'Présent' if self.present else 'Absent'}"

    # adherents/models.py

    from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

from django.db import models

class Intervenant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255, default='Unknown')
    telephone = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    cours_id = models.IntegerField(null=True)

    # Champs requis pour l'authentification
    username = models.CharField(max_length=150, unique=True, default='Unknown')
    email = models.EmailField(max_length=255, unique=True, default='Unknown')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Champ de mot de passe
    password = models.CharField(max_length=128, default='Unknown')
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'intervenant'