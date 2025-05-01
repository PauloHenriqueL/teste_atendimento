from django.contrib import admin
from . import models


class SessaoAdmin(admin.ModelAdmin):
    list_display = ('pk_sessao', 'dia_sessao')
    search_fields = ('pk_sessao',)

admin.site.register(models.Sessao, SessaoAdmin)