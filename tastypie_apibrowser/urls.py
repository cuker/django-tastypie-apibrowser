try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from views import StaffTemplateView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^$',
        StaffTemplateView.as_view(), name='api-browser'
    ),
    url(
        r'^templates$',
        TemplateView.as_view(template_name='apibrowser/templates.html'),
        name='api-browser-templates'
    )
)
