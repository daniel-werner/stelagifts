from django.db import models
from django.utils.translation import ugettext_lazy as _

class ContactMessage(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("Name"))
    email = models.EmailField(max_length=500, verbose_name=_("Email"))
    subject = models.CharField(max_length=1000, verbose_name=_("Subject"))
    message = models.TextField(max_length=4000, verbose_name=_("Message"))
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)    

    def status(self):
        if self.read:
            retVal = _("Read")
        else:
            retVal = _("Unread")

        return retVal

    class Meta:
        app_label = 'contact'    
