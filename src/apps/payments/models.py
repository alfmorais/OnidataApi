from uuid import uuid4

from django.db import models
from loans.models import Loans


class Payment(models.Model):
    id = models.UUIDField(
        verbose_name="Identificador",
        primary_key=True,
        default=uuid4,
    )
    loan = models.ForeignKey(
        Loans,
        models.CASCADE,
        verbose_name="Empréstimo",
        blank=False,
        null=False,
    )
    installment_amount = models.DecimalField(
        verbose_name="Valor do Empréstimo",
        max_digits=10,
        decimal_places=2,
    )
    installment_number = models.IntegerField(
        verbose_name="Identificador da Parcela do Empréstimo",
        blank=False,
        null=False,
    )
    date = models.DateTimeField(
        verbose_name="Data de Solicitação do Empréstimo",
        db_index=True,
        default=None,
    )
    is_paid = models.BooleanField(
        verbose_name="Parcela foi paga?",
        default=False,
    )

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self) -> str:
        return f"ID: {self.id} - Amount: {self.amount}"
