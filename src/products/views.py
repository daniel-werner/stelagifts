# Create your views here.
from django.utils.translation import ugettext as _
from django.template import loader, RequestContext
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from products.models import *
from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from products.models.device import Device
from django.template.defaultfilters import slugify
from django.conf.locale import tr


def index(request):
    request.breadcrumbs(_("Products"), reverse(index))

    product_list = Product.objects.filter(visible=True).order_by('-created')
    paginator = Paginator(product_list, 6) # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    t = loader.get_template('products/list.html')
    c = RequestContext(request, {
                                 "products":products,
                                 })    
    return HttpResponse(t.render(c))

def details(request, product_id, slug):
    request.breadcrumbs(_("Products"), reverse(index))
    try:
        product = Product.objects.get(id=product_id, visible=True)
    except Product.DoesNotExist:
        raise Http404
    
    if slug != slugify(product.name):
        return redirect('products.views.details', permanent=False, product_id=product_id, slug=slugify(product.name))
    
    productImages = product.productimage_set.all().order_by('-default')
    relatedProducts = product.related.all()
    productSizes = product.productsize_set.all()
    relatedDevices = product.devices.all()
    
    request.breadcrumbs(product,reverse(details, args=[product_id, slug]))
    t = loader.get_template('products/details.html')
    c = RequestContext(request, {
                                 "product": product,
                                 "productImages":productImages,
                                 "relatedProducts":relatedProducts,
                                 "productSizes":productSizes,
                                 "relatedDevices":relatedDevices
                                 });    
    return HttpResponse(t.render(c))

def tags(request, device_id, slug=None):
    request.breadcrumbs(_("Tags"),"#")

    product_list = Product.objects.filter( devices__pk=device_id, visible=True)
    paginator = Paginator(product_list, 6) # Show 25 contacts per page

    try:
        tag = Device.objects.get(pk=device_id);
    except Device.DoesNotExist:
        raise Http404

    if slug != slugify(tag.name):
        return redirect('products.views.tags', permanent=False, device_id=device_id, slug=slugify(tag.name))

    request.breadcrumbs(tag, reverse(tags, args=[device_id,slug]))

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    t = loader.get_template('products/tag_list.html')
    c = RequestContext(request, {
                                 "products":products,
                                 "tag":tag
                                 })    
    return HttpResponse(t.render(c))    
    
    