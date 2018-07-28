from django.db import models
from product import Product

# Create your models here.

class ProductSize(models.Model):
    product = models.ForeignKey(Product)    
    width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)
    
    class Meta:
        app_label = 'products'