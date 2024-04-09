from rest_framework import serializers
from .models import Vida
from planos.models import Plano
from django.shortcuts import get_object_or_404

class VidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vida
        fields = "__all__"

    def validate_idade(self, value):
        if value < 0:
            raise serializers.ValidationError("A idade não pode ser negativa.")
        return value

    def validate_plano(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "O ID do plano deve ser um valor positivo."
            )
        return value

    def create(self, validated_data):
        plano_id = validated_data.pop("plano_id")
        plano = get_object_or_404(Plano, id=plano_id)
        vida = Vida.objects.get_or_create(**validated_data)
        vida.planos.add(plano)

        return vida
