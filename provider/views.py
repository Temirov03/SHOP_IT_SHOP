from django.shortcuts import render
from .models import Provider,Income,IncomeItem
from .serializers import ProviderSerializer,IncomeSerializer,IncomeItemSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeItemViewSet(ModelViewSet):
    queryset = IncomeItem.objects.all()
    serializer_class = IncomeItemSerializer