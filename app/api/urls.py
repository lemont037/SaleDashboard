from django.urls import path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sales API",
      default_version='v1',
      description="Documentação da API para gerenciamento de vendas e canais de vendas.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('sales/', views.list_sales, name='api_sales_list'),
    path('sales/create/', views.create_sale, name='api_sales_create'),
    path('create_salesChannel/<str:name>', views.create_salesChannel, name='api_salesChannel_create'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]