from rest_framework import serializers
from .models import Provider,Income,IncomeItem

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'



class IncomeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Income
        fields = '__all__'



class IncomeItemSerializer(serializers.ModelSerializer):



    class Meta:
        model = IncomeItem
        fields = '__all__'