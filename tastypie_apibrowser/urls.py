from django.conf.urls.defaults import *
from views import staff_member_template

urlpatterns = patterns('', 
    (r'^$', staff_member_template, {'template':'apibrowser/index.html'}, 
        'api-browser'),
    )

