from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buggydebugger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.BlogIndex.as_view(), name="index")

)
