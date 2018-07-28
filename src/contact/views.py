# Create your views here.
from contact.forms.contactform import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.template import loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from breadcrumbs.utils import breadcrumbs_for_flatpages
from multilingual.flatpages.models import MultilingualFlatPage
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from products.models.product import Product

def contact(request, product_id=None):
    
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save(True);
            messages.info(request, _('Your message has been sent. Thank you for interesting to our products. Our crew will contact you soon.'))
            return HttpResponseRedirect(reverse(contact)) # Redirect after POST
    else:
        form = ContactForm() # An unbound form
                
        if product_id != None:
            product = Product.objects.get(pk=product_id)
            if product:
                form = ContactForm(initial={"subject":product.name})

    f = get_object_or_404(MultilingualFlatPage, url__exact='/contact/', sites__id__exact=settings.SITE_ID)
    #breadcrumbs
    #if f: breadcrumbs_for_flatpages(request,f)
    request.breadcrumbs(f.title, reverse(contact))
    
    t = loader.get_template('contacts/contact.html')
    c = RequestContext(request , {
                        "form":form,
                        "flatpage":f
                                  })    
    return HttpResponse(t.render(c))