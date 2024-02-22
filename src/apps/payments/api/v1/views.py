"""
TODO: Views não ficaram enxutas, métodos post e get foram sobrescritos
desnecessariamente mesmo sem o cénario de obtenção do IP.
"""

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

from .serializers import (
    BalanceSerializer,
    PaymentSerializer,
    PaymentUpdateSerializer,
)
from .services import BalanceService, PaymentListService, PaymentUpdateService


class PaymentListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, loan_uuid):
        service = PaymentListService()
        payments_queryset = service.handle(loan_uuid)
        response = PaymentSerializer(payments_queryset, many=True).data
        return Response({"data": response}, status=HTTP_200_OK)


class PaymentUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        service = PaymentUpdateService()
        serializer = PaymentUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = service.handle(request.data)
        response = PaymentSerializer(data, many=False).data
        return Response({"data": response}, status=HTTP_201_CREATED)


class BalanceListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, loan_uuid):
        service = BalanceService()
        data = service.handle(loan_uuid)
        response = BalanceSerializer(data, many=False).data
        return Response({"data": response}, status=HTTP_200_OK)
