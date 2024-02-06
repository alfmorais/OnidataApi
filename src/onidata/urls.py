from apps.loans.api.v1.views import LoansListAndCreateView
from apps.payments.api.v1.views import (
    BalanceListView,
    PaymentListAndUpdateView,
)
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

loans_patterns = [
    path("", LoansListAndCreateView.as_view(), name="list_and_create"),
]

payments_patters = [
    path(
        "<uuid:loan_uuid>/",
        PaymentListAndUpdateView.as_view(),
        name="list_and_update",
    ),
    path("<uuid:loan_uuid>/balance/", BalanceListView.as_view(), name="list"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("v1/loans/", include((loans_patterns, "loans"))),
    path("v1/payments/", include((payments_patters, "payments"))),
]
