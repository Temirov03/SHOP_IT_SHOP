from django.db import models

# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nomi',null=True)
    count = models.SmallIntegerField(verbose_name="Soni")
