from rest_framework import serializers
from .models import Locale


class LocaleSerializer(serializers.ModelSerializer):
    # chbre_proche = LocaleSerializer(many=True)
    class Meta:
        model = Locale
        fields = (
            'id',
            'ville',
            'commune',
            'libelle',
            'type_equipement',
            'profondeur_cable',
            'latitude',
            'longitude',
            'concessionnaire',
            'chbre_proche',
            'dtce_chambre_proche',
        )
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['chbre_proche'] = LocaleSerializer(instance.chbre_proche).data
        return response