from django.conf.urls.defaults import *
from views import staff_member_template
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('', 
    (r'^$',           staff_member_template, 
                      {'template':'apibrowser/index.html'}, 
                      'api-browser'),
    (r'^templates$', direct_to_template, 
                      {'template':'apibrowser/templates.html'},
                      'api-browser-templates'),
    )

