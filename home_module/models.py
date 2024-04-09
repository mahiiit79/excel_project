from django.db import models



class ProductTable(models.Model):
    title = models.CharField(max_length=300,verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد محصول')
    is_active = models.BooleanField(verbose_name='موجودی')
