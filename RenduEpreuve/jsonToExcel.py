import json
import pandas as pd

# Charger le JSON depuis le fichier
with open('fonctionnalites_systeme_gestion.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Préparer les données pour le DataFrame
fonctionnalites = data['fonctionnalites']
formatted_data = []

for fonctionnalite in fonctionnalites:
    nom = fonctionnalite['nom']
    description = fonctionnalite['description']
    priorite = fonctionnalite['priorite']
    etat = fonctionnalite['etat']
    responsable = fonctionnalite['responsable']
    date_livraison_prevue = fonctionnalite['date_livraison_prevue']

    # Joindre les besoins techniques en une seule chaîne
    besoins_techniques = "\n".join(fonctionnalite['besoins_techniques'])

    formatted_data.append({
        'Nom': nom,
        'Description': description,
        'Priorité': priorite,
        'État': etat,
        'Responsable': responsable,
        'Date de livraison prévue': date_livraison_prevue,
        'Besoins techniques': besoins_techniques
    })

# Créer un DataFrame
df = pd.DataFrame(formatted_data)

# Sauvegarder le DataFrame en fichier Excel
df.to_excel('fonctionnalites.xlsx', index=False)

print("Le fichier Excel a été généré avec succès.")
