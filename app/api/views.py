from django.conf import settings
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import SaleSerializer, SaleChannelSerializer
from .models import Sale
from django.utils import timezone
from datetime import datetime

@swagger_auto_schema(
    method='post',
    operation_description="Cria um novo Canal de Vendas.",
    request_body=SaleChannelSerializer,
    responses={201: SaleChannelSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_salesChannel(request, name):
    serializer = SaleChannelSerializer(data={"name": name.lower()})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        errors = serializer.errors
        return Response({"errors": errors}, status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    operation_description="Cria uma nova venda.",
    request_body=SaleSerializer,
    responses={201: SaleSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_sale(request):
    new_sale = request.data

    serializer = SaleSerializer(data=new_sale)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        errors = serializer.errors
        return Response({"errors": errors}, status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description="Lista as vendas com filtros opcionais.",
    manual_parameters=[
        openapi.Parameter('period_from', openapi.IN_QUERY, description="Data de início do período (formato: D/M/Y H:M:S)", type=openapi.TYPE_STRING),
        openapi.Parameter('period_to', openapi.IN_QUERY, description="Data de fim do período (formato: D/M/Y H:M:S)", type=openapi.TYPE_STRING),
        openapi.Parameter('state', openapi.IN_QUERY, description="Estado para filtrar vendas", type=openapi.TYPE_STRING),
        openapi.Parameter('sale_channel', openapi.IN_QUERY, description="Canal de venda para filtrar vendas", type=openapi.TYPE_STRING),
    ],
    responses={200: SaleSerializer(many=True), 400: 'Bad Request'}
)
@api_view(['GET'])
def list_sales(request):

    # Getting filters parameters
    period_from = request.GET.get('period_from', False)
    period_to = request.GET.get('period_to', False)
    state = request.GET.get('state', False)
    sale_channel = request.GET.get('sale_channel', False)

    # Creating dynamic filter
    filters = Q()

    if period_from or period_to:
        if period_from:
            try:
                period_from = datetime.strptime(period_from, settings.DATETIME_MASK)
            except:
                error = {
                            "error": "Invalid search parameter",
                            "details": "O valor fornecido para 'Data Início' não é válido. Por favor, forneça uma data no formato 'D/M/Y H:M:S'."
                        }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            period_from = timezone.make_aware(period_from)
        else:
            period_from = timezone.make_aware(datetime.min)
        
        if period_to:
            try:
                period_to = datetime.strptime(period_to, settings.DATETIME_MASK)
            except:
                error = {
                            "error": "Invalid search parameter",
                            "details": "O valor fornecido para 'Data Fim' não é válido. Por favor, forneça uma data no formato 'D/M/Y H:M:S'."
                        }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            period_to = timezone.make_aware(period_to)
        else:
            period_to = timezone.make_aware(datetime.now())
        
        filters &= Q(date__range=(period_from, period_to))

    if state:
        filters &= Q(state=state)

    if sale_channel:
        #sale_channel = SaleChannel.objects.get(name=sale_channel.lower())['id']
        filters &= Q(sale_channel__name=sale_channel.lower())

    sales = Sale.objects.filter(filters)

    serializer = SaleSerializer(sales, many=True)

    return Response(serializer.data)