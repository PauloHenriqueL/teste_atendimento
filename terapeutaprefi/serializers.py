from rest_framework import serializers
from terapeutaprefi.models import Tprefeidade


class PrefeidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tprefeidade
        fields = '__all__'
