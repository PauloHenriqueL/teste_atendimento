from rest_framework import serializers
from sessao.models import Sessao


class SessaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessao
        fields = '__all__'
