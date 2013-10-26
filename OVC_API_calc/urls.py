from django.conf.urls import patterns, include, url
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'calcula', views.OperacionViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OVC_API_calc.views.home', name='home'),
    # url(r'^OVC_API_calc/', include('OVC_API_calc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
