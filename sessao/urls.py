from django.urls import path
from . import views


urlpatterns = [
    path('sessao', views.SessaoCreateListView.as_view(), name='sessao-list'),
    path('sessao/<int:pk>', views.SessaoRetrieveUpdateDestoyView.as_view(), name='sessao-update'),
]
