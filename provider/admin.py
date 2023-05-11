from django.contrib import admin
from provider.models import Provider,Income,IncomeItem
# Register your models here.
admin.site.register([Provider,Income,IncomeItem])
