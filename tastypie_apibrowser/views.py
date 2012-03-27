from django.views.generic.simple import direct_to_template
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def staff_member_template(*args, **kwargs):
    return direct_to_template(*args, **kwargs)    

