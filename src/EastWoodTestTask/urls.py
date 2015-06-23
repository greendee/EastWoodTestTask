from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'EastWoodTestTask.views.home', name='home'),
    # url(r'^EastWoodTestTask/', include('EastWoodTestTask.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^employees/', include("employees.urls", namespace='employees')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
