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


class PaymentListAndUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, loan_uuid):
        # TODO: Colocar um filtro django para listar se é pago ou não.
        service = PaymentListService()
        payments_queryset = service.handle(loan_uuid, is_paid=True)
        response = PaymentSerializer(payments_queryset, many=True).data
        return Response({"data": response}, status=HTTP_200_OK)

    def put(self, request, loan_uuid):
        service = PaymentUpdateService()
        serializer = PaymentUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = service.handle(loan_uuid, request.data)
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
