import requests

# URL de base de votre API Django
base_url = 'http://localhost:8000/'

# Endpoint pour lister les adhérents
list_adherents_url = base_url + 'api/adherents/'

# Endpoint pour envoyer une notification à un adhérent spécifique
send_notification_url = base_url + 'api/adherents/1/send_notification/'  # Remplacez 1 par l'ID d'un adhérent existant

# Endpoint pour enregistrer les présences
enregistrer_presences_url = base_url + 'api/presences/'

# Endpoint pour lister les présences enregistrées
list_presences_url = base_url + 'api/presences/list/'

# Endpoint pour enregistrer les adhérents sélectionnés
save_selected_adherents_url = base_url + 'api/save-selected-adherents/'

# Endpoint pour effectuer une authentification
login_url = base_url + 'api/login/'

# Endpoint pour obtenir un token JWT
token_url = base_url + 'api/token/'

# Endpoint pour rafraîchir le token JWT
refresh_token_url = base_url + 'api/token/refresh/'

# Endpoint pour mettre à jour la présence d'un adhérent spécifique
update_presence_url = base_url + 'api/adherents/1/'  # Remplacez 1 par l'ID d'un adhérent existant

# Exemple de corps de requête pour l'enregistrement des présences
presences_data = {
    "1": True,
    "2": False,
    "3": True
}

# Exemple de corps de requête pour la mise à jour de la présence d'un adhérent
update_presence_data = {
    "present": True
}

def test_list_adherents():
    response = requests.get(list_adherents_url)
    print(f"Liste des adhérents - Statut: {response.status_code}")
    print(response.json())

def test_send_notification():
    response = requests.post(send_notification_url)
    print(f"Envoi de notification à l'adhérent - Statut: {response.status_code}")
    print(response.json())

def test_enregistrer_presences():
    response = requests.post(enregistrer_presences_url, json=presences_data)
    print(f"Enregistrement des présences - Statut: {response.status_code}")
    print(response.json())

def test_list_presences():
    response = requests.get(list_presences_url)
    print(f"Liste des présences enregistrées - Statut: {response.status_code}")
    print(response.json())

def test_save_selected_adherents():
    response = requests.post(save_selected_adherents_url)
    print(f"Enregistrement des adhérents sélectionnés - Statut: {response.status_code}")
    print(response.json())

def test_login():
    response = requests.post(login_url)
    print(f"Connexion - Statut: {response.status_code}")
    print(response.json())

def test_get_token():
    response = requests.post(token_url)
    print(f"Obtention du token JWT - Statut: {response.status_code}")
    print(response.json())

def test_refresh_token():
    response = requests.post(refresh_token_url)
    print(f"Rafraîchissement du token JWT - Statut: {response.status_code}")
    print(response.json())

def test_update_presence():
    response = requests.put(update_presence_url, json=update_presence_data)
    print(f"Mise à jour de la présence d'un adhérent - Statut: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    test_list_adherents()
    test_send_notification()
    test_enregistrer_presences()
    test_list_presences()
    test_save_selected_adherents()
    test_login()
    test_get_token()
    test_refresh_token()
    test_update_presence()
