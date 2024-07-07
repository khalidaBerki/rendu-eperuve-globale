import json
from openpyxl import Workbook

# Données JSON
data = {
  "fonctionnalites": [
    {
      "nom": "Gestion des Adhérents",
      "description": "Cette fonctionnalité permet la création, la modification et la suppression des profils d'adhérents...",
      "performance_evaluee": "La fonctionnalité est complétée avec la gestion des profils et des informations personnelles. Les notifications de cotisation sont opérationnelles.",
      "points_amelioration": [
        "Tester la scalabilité avec un grand nombre d'adhérents.",
        "Assurer la stabilité des notifications de cotisation."
      ]
    },
    {
      "nom": "Gestion des Événements",
      "description": "Cette fonctionnalité permet de planifier, organiser et gérer des événements pour les adhérents...",
      "performance_evaluee": "En cours de développement avec la planification et la gestion des inscriptions en progression.",
      "points_amelioration": [
        "Intégrer et tester le calendrier intégré pour assurer une planification efficace.",
        "Finaliser le module d'inscription en ligne avec gestion des statuts d'inscription."
      ]
    },
    {
      "nom": "Administration du Système",
      "description": "Cette fonctionnalité permet la création et la gestion des comptes administrateurs avec attribution de rôles...",
      "performance_evaluee": "À l'étude pour les fonctionnalités d'authentification et de gestion des rôles.",
      "points_amelioration": [
        "Définir clairement les besoins en journalisation pour assurer la conformité et la sécurité.",
        "Prévoir des tests approfondis de sécurité pour les comptes administrateurs."
      ]
    },
    {
      "nom": "Gestion des Cours",
      "description": "Cette fonctionnalité permet la création, l'édition et la suppression des cours proposés aux adhérents...",
      "performance_evaluee": "En phase d'étude pour la création et la gestion des cours avec une attention sur les workflows d'inscription.",
      "points_amelioration": [
        "Définir et tester des workflows d'inscription et de suivi des participants.",
        "Intégrer des notifications efficaces pour les nouvelles offres de cours."
      ]
    },
    {
      "nom": "Gestion des Intervenants",
      "description": "Cette fonctionnalité permet la création, la gestion et l'attribution des profils d'intervenants aux cours et événements...",
      "performance_evaluee": "En cours de développement avec création et gestion des profils d'intervenants.",
      "points_amelioration": [
        "Tester l'attribution dynamique des intervenants aux cours et événements.",
        "Assurer la gestion des notifications pour les mises à jour des intervenants."
      ]
    },
    {
      "nom": "Gestion des Ressources",
      "description": "Cette fonctionnalité permet la création, la gestion et la disponibilité des ressources physiques...",
      "performance_evaluee": "À l'étude pour la planification et la gestion des ressources physiques.",
      "points_amelioration": [
        "Intégrer un système d'inventaire avec gestion des conflits d'utilisation en temps réel.",
        "Tester la fiabilité du système de maintenance préventive avec alertes."
      ]
    },
    {
      "nom": "Communication et Notifications",
      "description": "Cette fonctionnalité permet l'envoi de notifications automatiques aux adhérents et intervenants...",
      "performance_evaluee": "À l'étude pour l'envoi de notifications multi-canaux et la personnalisation des messages.",
      "points_amelioration": [
        "Intégrer un module de suivi des réponses et des confirmations.",
        "Tester la fiabilité des systèmes de notifications multi-canaux."
      ]
    },
    {
      "nom": "Rapports et Analyses",
      "description": "Cette fonctionnalité permet de générer des rapports détaillés sur les inscriptions, les performances des adhérents...",
      "performance_evaluee": "À l'étude pour la génération de rapports personnalisables et les visualisations graphiques.",
      "points_amelioration": [
        "Assurer la sécurité des données analytiques et l'accès restreint aux rapports.",
        "Intégrer des visualisations graphiques pour faciliter l'analyse des données."
      ]
    }
  ]
}

# Création du fichier Excel
wb = Workbook()
ws = wb.active
ws.title = "Fonctionnalités"

# Écriture des en-têtes
headers = ["Nom", "Description", "Performance évaluée", "Points d'amélioration"]
ws.append(headers)

# Écriture des données
for fonctionnalite in data["fonctionnalites"]:
    row = [
        fonctionnalite["nom"],
        fonctionnalite["description"],
        fonctionnalite["performance_evaluee"],
        "\n".join(fonctionnalite["points_amelioration"])  # Points d'amélioration sur plusieurs lignes
    ]
    ws.append(row)

# Sauvegarde du fichier Excel
wb.save("poc.xlsx")

print("Fichier Excel généré avec succès.")
