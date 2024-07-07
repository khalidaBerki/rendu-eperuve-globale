from django.contrib.auth.hashers import make_password
from .models import Intervenant


def set_intervenant_password(username, new_password):
    try:
        # Récupérer l'intervenant par nom d'utilisateur
        intervenant = Intervenant.objects.get(username=username)

        # Hasher le nouveau mot de passe
        hashed_password = make_password(new_password)

        # Affecter le mot de passe hashé à l'intervenant
        intervenant.password = hashed_password

        # Sauvegarder l'intervenant pour enregistrer le mot de passe en base de données
        intervenant.save()

        return True  # Indiquer que le mot de passe a été mis à jour avec succès

    except Intervenant.DoesNotExist:
        return False  # Gérer l'erreur si l'intervenant n'existe pas
