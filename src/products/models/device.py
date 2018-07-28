from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=50)    
    created = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = 'products'