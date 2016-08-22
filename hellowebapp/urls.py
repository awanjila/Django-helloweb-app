
from django.conf.urls import patterns,include, url
from django.contrib import admin




from django.views.generic import TemplateView
from collection import views as collection_views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', collection_views.index, name='home'),
	url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
         name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),

	]
