from django.db import models
from django.utils import timezone
from atendimentos.models import AtendimentoMensal
from django.core.validators import MinValueValidator, MaxValueValidator


class Sessao(models.Model):
    pk_sessao = models.AutoField(primary_key=True)
    RESPONSAVEL_CHOICES = [
        ('TERAPEUTA', 'Terapeuta'),
        ('PACIENTE', 'Paciente'),
    ]
    fk_atendimento_mensal = models.ForeignKey(AtendimentoMensal, on_delete=models.CASCADE, related_name='sessoes', db_column='fk_atendimento_mensal')
    dia_sessao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], null=False)
    realizado = models.BooleanField(default=False, null=False)
    responsavel_cancelamento = models.CharField(max_length=10, choices=RESPONSAVEL_CHOICES, null=True, blank=True)
    pago = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def save(self, *args, **kwargs):
        # Implementa a restrição CHECK do PostgreSQL
        if self.realizado and self.responsavel_cancelamento is not None:
            raise ValueError("Quando a sessão é realizada, responsável_cancelamento deve ser NULL")
        if not self.realizado and self.responsavel_cancelamento is None:
            raise ValueError("Quando a sessão não é realizada, responsável_cancelamento deve ser preenchido")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sessao

    class Meta:
        db_table = "sessoes"
        unique_together = ('fk_atendimento_mensal', 'dia_sessao')