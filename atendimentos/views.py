from rest_framework import generics
from atendimentos.models import AtendimentoMensal
from atendimentos.serializers import AtendimentoSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AtendimentoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AtendimentoMensal.objects.all()
    serializer_class = AtendimentoSerializer


class AtendimentoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AtendimentoMensal.objects.all()
    serializer_class = AtendimentoSerializer
