from django.contrib import admin
from . import models

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('pk_atendimento_mensal', 'fk_decano', 'fk_terapeuta', 'fk_paciente')
    search_fields = ('pk_atendimento_mensal', 'fk_terapeuta')

admin.site.register(models.AtendimentoMensal, AtendimentoAdmin)