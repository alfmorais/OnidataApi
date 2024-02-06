from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView


class PaymentListAndUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, loan_uuid):
        return Response(
            {"message": "get", "id": loan_uuid},
            status=HTTP_200_OK,
        )

    def put(self, request, loan_uuid):
        return Response(
            {"message": "put", "id": loan_uuid, "data": request.data},
            status=HTTP_201_CREATED,
        )


class BalanceListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, loan_uuid):
        return Response(
            {"message": "get", "balance": True},
            status=HTTP_200_OK,
        )
