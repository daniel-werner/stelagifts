from multilingual.flatpages.models import MultilingualFlatPage
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
import multilingual
from breadcrumbs.utils import breadcrumbs_for_flatpages
import django.dispatch
from django.core.signals import request_started


DEFAULT_TEMPLATE = 'flatpages/default.html'

def multilingual_flatpage(request, url):
    """
    Multilingual flat page view.

    Models: `multilingual.flatpages.models`
    Templates: Uses the template defined by the ``template_name`` field,
        or `flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(MultilingualFlatPage, url__exact=url, sites__id__exact=settings.SITE_ID)
    #breadcrumbs
    if f: breadcrumbs_for_flatpages(request,f)
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    # Serve the content in the language defined by the Django translation module
    # if possible else serve the default language.
    f._default_language = get_language()
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    data = request_started.send(sender=MultilingualFlatPage,flatpage=f)
    
    if data.count > 1:
        data.pop(0);
    
    c = RequestContext(request, {
        'flatpage': f,
        'data':data,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, MultilingualFlatPage, f.id)
    return response
