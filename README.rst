API Viewer for Tastypie 
========================

This is a javascript-based API browser for tastypie - the JS requirements
are vendored in.  Out-of-the-box, this project adds the apibrowser to 
the admin, extending the ``admin/index.html`` template.

This has been tested on Django 1.3+, but should work anywhere that 
tastypie is installed.  

Installation
==============

Install by fetching the repository from github and installing::

    % git git@github.com:cuker/django-tastypie-apibrowser
    % python setup.py install

Then, open your settings.py and add the application to ``INSTALLED_APPS``::
    
    INSTALLED_APPS = (
    # .. apps ..
    'tastypie_apibrowser',
    # .. more apps ..
    )

   
Finally, add the following to your urlconf::
    
        (r'^admin/apibrowser/', include('tastypie_apibrowser.urls')) 

This line should go before your other admin urls.


     

