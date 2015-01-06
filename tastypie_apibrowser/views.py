from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def staff_member_template(*args, **kwargs):
    return TemplateView.as_view(*args, **kwargs)    

