from django.db import models
from decimal import Decimal

# Create your models here.
class SaleChannel(models.Model):
    name = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    states = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    ]
    
    date = models.DateTimeField(default=models.functions.Now())
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal("0.00"))
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal("0.00"))
    state = models.CharField(max_length=2, choices=states)
    sale_channel = models.ForeignKey(SaleChannel, on_delete=models.CASCADE)