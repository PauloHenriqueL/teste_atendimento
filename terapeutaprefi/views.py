from rest_framework import generics
from terapeutaprefi.models import Tprefeidade
from terapeutaprefi.serializers import TprefeidadeSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class TprefeidadeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Tprefeidade.objects.all()
    serializer_class = TprefeidadeSerializer


class TprefeidadeRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Tprefeidade.objects.all()
    serializer_class = TprefeidadeSerializer
