from management.models import Currency, ExchangesRate, Subscription
from users.models import CustomUser
from rest_framework.generics import ListAPIView
from management.serializers import (CurrenciesSerializer)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CurrenciesListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        queryset = Currency.objects.all()
        serializer = CurrenciesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.is_staff:
            input_serializer = CurrenciesSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            input_serializer.save()
            return Response(input_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

