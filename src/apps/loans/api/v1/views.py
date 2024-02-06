from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

from .serializers import LoanCreateSerializer, LoansSerializer
from .services import CreateLoanService, ListAllLoansService


class LoansListAndCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        service = ListAllLoansService()
        loans_queryset = service.handle(user_id)
        response = LoansSerializer(loans_queryset, many=True).data
        return Response({"data": response}, status=HTTP_200_OK)

    def post(self, request):
        user_id = request.user.id
        service = CreateLoanService()
        serializer = LoanCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = service.handle(user_id, serializer.data)
        response = LoansSerializer(data, many=False).data
        return Response({"data": response}, status=HTTP_201_CREATED)
