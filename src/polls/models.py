from django.db import models
import datetime
from polls.multiling import MultilingualModel

# Create your models here.

class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.name    

class PollTranslation(models.Model):
    language = models.ForeignKey("Language",blank=False, null=False);
    question = models.CharField(max_length=200)
    model = models.ForeignKey("Poll")

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