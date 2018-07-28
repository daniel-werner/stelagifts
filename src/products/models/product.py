from django.db import models
from multilingual.translation import TranslationModel
from multilingual.translation import Translation as TranslationBase
from multilingual.manager import MultilingualManager
from multilingual.exceptions import TranslationDoesNotExist
from products.models.device import Device
from multilingual.flatpages.models import MultilingualFlatPage
from django.core.signals import request_started

# Create your models here.

class Product(models.Model):
    related = models.ManyToManyField('self', blank=True, null=True)
    devices = models.ManyToManyField( Device,blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)
    visible = models.BooleanField(db_index=True)
    stock = models.BooleanField(db_index=True)
    
    objects = MultilingualManager()
    
    class Translation(TranslationBase):
        name = models.CharField(max_length=255)
        description = models.CharField(max_length=1000, blank=True, null=True)
        material = models.CharField(max_length=400, blank=True, null=True)
    
    class Meta:
        app_label = 'products'
  
    def __unicode__(self):
        # note that you can use name and description fields as usual
        try:
            return u"%s" % (self.name)
        except TranslationDoesNotExist:
            return u"-not-available-"
    
    def get_default_image(self):
        return self.productimage_set.all().order_by('-default')[:1][0]
    

def get_for_sidebar(sender, **kwargs):
    data = Product.objects.filter(visible=True).all()
    return data;
    
request_started.connect(get_for_sidebar, sender=MultilingualFlatPage)  
        
"""
class Poll(MultilingualModel):
    pub_date = models.DateTimeField('date published')
    
    class Meta:
        translation = PollTranslation
        multilingual = ['question']
    
    def __unicode__(self):
        return self.question
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice   
        """