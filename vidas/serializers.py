from rest_framework import serializers
from .models import Vida
from planos.models import Plano
from django.shortcuts import get_object_or_404


class VidaSerializer(serializers.ModelSerializer):
    planos = serializers.PrimaryKeyRelatedField(queryset=Plano.objects.all(), many=True)

    class Meta:
        model = Vida
        fields = "__all__"

    def validate_idade(self, value):
        if value < 0:
            raise serializers.ValidationError("A idade não pode ser negativa.")
        return value

    def create(self, validated_data):
        planos_lista = validated_data.pop("planos", [])
        vida, created = Vida.objects.get_or_create(**validated_data)


        for plano in planos_lista:
            plano_em_sistema = get_object_or_404(Plano, id=plano.id)
            plano_em_sistema.vidas.add(vida)

        return vida
