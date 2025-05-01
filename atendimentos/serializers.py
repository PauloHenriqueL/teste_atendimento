from rest_framework import serializers
from atendimentos.models import AtendimentoMensal


class AtendimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtendimentoMensal
        fields = '__all__'
