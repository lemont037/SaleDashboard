from django.shortcuts import render
from django.db.models import F, Sum
from api.models import Sale

def dashboard(request):
    return render(request, 'dashboard.html')