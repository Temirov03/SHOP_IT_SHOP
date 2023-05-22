from django.contrib import admin
from .models import Category,Product,Manufactory,Country,Character,ProductMedia,ProductCharacter,ProductPrice

# Register your models here.
admin.site.register([Category,Product,Manufactory,Country,Character,ProductMedia,ProductCharacter,ProductPrice])
