from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from accounts.dashboard.app import application as accounts_app
from accounts.views import AccountBalanceView

from gap.views import product_options, get_quote
from apps.app import application
#from oscar.app import application

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^checkout/paypal/', include('paypal.express.urls')),
    (r'^dashboard/accounts/', include(accounts_app.urls)),

    url(r'^giftcard-balance/', AccountBalanceView.as_view(),
        name="account-balance"),
    url(r'^product-options/(?P<product_id>\d+)/$', product_options, name='product_options'),
    url(r'^get-quote/(?P<id>\d+)/$', get_quote, name='get_quote'),

    (r'', include(application.urls))
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT,'show_indexes': True}),
#        (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}),
#)
