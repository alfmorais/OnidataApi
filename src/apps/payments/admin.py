from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "loan",
        "installment_amount",
        "date",
        "is_paid",
    ]
    fields = [
        "id",
        "loan",
        "installment_amount",
        "date",
        "is_paid",
    ]

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False
