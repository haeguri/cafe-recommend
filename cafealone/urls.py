from django.conf.urls import include, url
from django.contrib import admin
from main.views import api_cafe, api_cafe_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'cafealone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/cafes/$', api_cafe),
    url(r'^api/cafes/(?P<pk>\d+)$', api_cafe_detail),

    url(r'^', include('main.urls')),
]
