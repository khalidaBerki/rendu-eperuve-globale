import json
from django.core.management.base import BaseCommand
from adherents.models import Adherent, ResponsableLegal

class Command(BaseCommand):
    help = 'Importe des adhérents depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        file_path = 'data/adherents.json'  # Chemin relatif vers votre fichier adherents.json

        with open(file_path, 'r') as file:
            adherents_data = json.load(file)

            for adherent_data in adherents_data:
                if 'responsable_legal' in adherent_data:
                    responsable_legal_data = adherent_data.pop('responsable_legal')
                    responsable_legal = ResponsableLegal.objects.create(**responsable_legal_data)
                    adherent_data['responsable_legal'] = responsable_legal

                Adherent.objects.create(**adherent_data)

        self.stdout.write(self.style.SUCCESS('Importation terminée avec succès'))
