from django.contrib import admin
from . import models


class TerapeutaprefiAdmin(admin.ModelAdmin):
    list_display = ('pk_terapeuta_prefeidade', 'fk_terapeuta')
    search_fields = ('pk_terapeuta_prefeidade', 'fk_terapeuta')

admin.site.register(models.Tprefeidade, TerapeutaprefiAdmin)