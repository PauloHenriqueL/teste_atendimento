from rest_framework import generics
from sessao.models import Sessao
from sessao.serializers import SessaoSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class SessaoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer


class SessaoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
