try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from views import staff_member_template

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    (
        r'^$',
        staff_member_template,
        {'template': 'apibrowser/index.html'}, 'api-browser'
    ),
    url(
        r'^templates$',
        TemplateView.as_view(template_name='apibrowser/templates.html'),
        name='api-browser-templates'
    )
)
