from django.db import models
from django.utils import timezone
from prefeidades.models import Prefeidade
from terapeuta.models import Terapeuta

class Tprefeidade(models.Model):
    pk_terapeuta_prefeidade = models.AutoField(primary_key=True)
    fk_terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, db_column='fk_terapeuta')
    fk_prefeidade = models.ForeignKey(Prefeidade, on_delete=models.CASCADE, db_column='fk_prefeidade')
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


    class Meta:
        managed = False
        db_table = '"hamilton"."terapeutas_prefeidades"'
