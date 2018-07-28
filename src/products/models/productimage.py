from django.db import models
from imagemodel import ImageModel
from product import Product


class ProductImage(ImageModel):
    product = models.ForeignKey(Product)
    
    class Meta:
        app_label = 'products'    