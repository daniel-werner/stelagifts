'''
Created on Jan 16, 2011

@author: vernerd
'''

from django import forms
from django.forms.models import ModelForm
from contact.models import ContactMessage
from django.forms import Textarea
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _


class ContactForm(ModelForm):
    security_code = CaptchaField(label=_("Security code"))
    class Meta:
        model=ContactMessage
        exclude = ( 'read', 'created', 'modified', )        
        
'''        
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
'''