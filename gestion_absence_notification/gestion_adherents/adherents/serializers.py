# adherents/serializers.py

from rest_framework import serializers
from .models import Adherent, Presence

class AdherentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adherent
        fields = '__all__'

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'

from rest_framework import serializers
from .models import Intervenant

class IntervenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervenant
        fields = ('id', 'username', 'password', 'adresse', 'telephone', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Intervenant.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            adresse=validated_data.get('adresse', ''),
            telephone=validated_data.get('telephone', ''),
            role=validated_data.get('role', '')
        )
        return user