from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('Category',verbose_name='Kategoriyasi',on_delete=models.PROTECT,
                               null=True,blank=True)
    name = models.CharField(verbose_name='Kategoriya nomi',max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category',verbose_name='Kategoriyasi',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Maxsulot nomi', max_length=255)
    full_name = models.CharField(verbose_name="Maxsulotning to'liq nomi",max_length=255)
    price = models.DecimalField(verbose_name='Maxsulot narxi',max_digits=100000000, decimal_places=2)
    descrpition = models.TextField(verbose_name="Maxsulot haqida malumot")



    def __str__(self):
        return self.full_name
