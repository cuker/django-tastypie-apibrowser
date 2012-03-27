from django.conf.urls.defaults import *
from views import direct_to_template

urlpatterns = patterns('', 
    (r'^$', direct_to_template, {'template':'apibrowser/index.html'}, 
        'api-browser'),
    )

