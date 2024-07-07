 Gestion des Absences et Notifications - Application Django + React

Ce projet est une application web développée avec Django pour le backend et React pour le frontend. Il offre des fonctionnalités de gestion des adhérents et des absences au sein d'une association.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :
- Python 3.x
- Node.js et npm (pour exécuter le frontend React)
- Git

## Clonage du Projet

Pour cloner ce projet depuis GitHub et le configurer sur votre machine locale, suivez ces étapes :

1. Ouvrez un terminal ou une invite de commande.

2. Clonez le dépôt avec la commande suivante :
   ```bash
   git clone https://github.com/khalidaBerki/rendu-eperuve-globale.git
   ```

3. Naviguez dans le répertoire du projet :
   ```bash
   cd rendu-eperuve-globale/gestion_absence_notification
   cd frontend
   ```

4. Activez votre environnement virtuel (si ce n'est pas déjà fait) :
   ```bash
   # Sous Windows (utilisant Command Prompt ou PowerShell)
   venv\Scripts\activate

   # Sous macOS/Linux
   source venv/bin/activate
   ```

5. Installez les dépendances Python à partir du fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```

6. Appliquez les migrations de base de données Django :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Démarrez le serveur Django :
   ```bash
   python manage.py runserver
   ```

8. Dans un autre terminal, naviguez vers le dossier frontend pour démarrer le serveur React :
   ```bash
   cd frontend
   npm install
   npm start
   ```

9. Accédez à l'application dans votre navigateur à l'adresse suivante :
   ```plaintext
   http://localhost:3000/
   ```

## Utilisation

- Connectez-vous à l'application et explorez les différentes fonctionnalités de gestion des adhérents et des absences.

  http://localhost:3000/api/adherents

  http://localhost:3000/api/presences

  http://localhost:8000/admin/

   user : admin mot de pass: admin (je sais que je ne suis pas sensée le mettre ici mais je n'ai pas eu le temps de le encoder ) 


