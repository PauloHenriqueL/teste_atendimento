from django.urls import path
from . import views


urlpatterns = [
    path('tprefeidade', views.TprefeidadeCreateListView.as_view(), name='tprefeidade-list'),
    path('tprefeidade/<int:pk>', views.TprefeidadeRetrieveUpdateDestoyView.as_view(), name='tprefeidade-update'),
]
