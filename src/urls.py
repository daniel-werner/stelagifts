from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
    (r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),    
    (r'^ckeditor/', include('ckeditor.urls')),
    
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += patterns('views',
    #(r'^$', 'construct'),
    (r'^$', 'index'),
    #(r'^localeurl/', include('localeurl.urls')),
    )

urlpatterns += patterns('products.views',
    (r'^products/$', 'index'),
    (r'^products/(?P<product_id>\d+)-(?P<slug>[a-zA-Z0-9_.-]+)/$', 'details'),
    (r'^products/tags/(?P<device_id>\d+)-(?P<slug>[a-zA-Z0-9_.-]+)/$', 'tags'),    
    #(r'^localeurl/', include('localeurl.urls')),
    )

urlpatterns += patterns('',
    (r'^contact/(?P<product_id>\d+)/$', 'contact.views.contact'),
    (r'^contact/$', 'contact.views.contact'),
    ('^', include('multilingual.flatpages.urls')),                                                 
    )
    