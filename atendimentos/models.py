from django.db import models
from django.utils import timezone
from decano.models import Decano
from terapeuta.models import Terapeuta
from paciente.models import Paciente
from django.core.validators import MinValueValidator, MaxValueValidator


class AtendimentoMensal(models.Model):
    pk_atendimento_mensal = models.AutoField(primary_key=True)
    mes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=False)
    ano = models.IntegerField(null=False)
    fk_decano = models.ForeignKey(Decano, on_delete=models.CASCADE, related_name='atendimentos_mensais', db_column='fk_decano')
    fk_terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, related_name='atendimentos_mensais', db_column='fk_terapeuta')
    fk_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='atendimentos_mensais', db_column='fk_paciente')
    qtd_sessoes = models.IntegerField(validators=[MinValueValidator(1)], null=False)
    vlr_sessao = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False)
    vlr_pago_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Atendimento {self.pk_atendimento} - Paciente: {self.fk_paciente.nome}"

    class Meta:
        managed = False
        unique_together = ('mes', 'ano', 'fk_terapeuta', 'fk_paciente')
        db_table = '"hamilton"."atendimentos_mensais"'